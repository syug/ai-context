#!/usr/bin/env python3
"""
Asana Weekly Summary — AI Mission Control time tracking report.

Fetches completed tasks from the AI Mission Control project for a given week,
calculates durations, and outputs a Markdown summary grouped by project category.

Usage:
    python3 asana-weekly-summary.py [--week YYYY-MM-DD]

    --week: Monday of the target week (default: current week's Monday)
"""

import argparse
import os
import re
import sys
from datetime import datetime, timedelta, timezone

try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install with: pip3 install requests", file=sys.stderr)
    sys.exit(1)

PROJECT_GID = "1213488615214853"
BASE_URL = "https://app.asana.com/api/1.0"

# ---------------------------------------------------------------------------
# Asana API helpers
# ---------------------------------------------------------------------------

def get_headers():
    pat = os.environ.get("ASANA_PAT")
    if not pat:
        print("Error: ASANA_PAT environment variable is not set.", file=sys.stderr)
        sys.exit(1)
    return {"Authorization": f"Bearer {pat}", "Accept": "application/json"}


def asana_get(path, params=None):
    """GET request with automatic pagination."""
    headers = get_headers()
    url = f"{BASE_URL}{path}"
    all_data = []
    while url:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        body = resp.json()
        all_data.extend(body.get("data", []))
        next_page = body.get("next_page")
        if next_page and next_page.get("uri"):
            url = f"https://app.asana.com{next_page['uri']}" if next_page["uri"].startswith("/") else next_page["uri"]
            params = None  # params are already embedded in the URI
        else:
            url = None
    return all_data


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def get_week_monday(date_str=None):
    """Return the Monday of the specified or current week."""
    if date_str:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    else:
        dt = datetime.now()
    monday = dt - timedelta(days=dt.weekday())
    return monday.replace(hour=0, minute=0, second=0, microsecond=0)


def fmt_date(iso_str):
    """Parse ISO-8601 date string from Asana."""
    if not iso_str:
        return None
    return datetime.fromisoformat(iso_str.replace("Z", "+00:00"))


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def fetch_completed_tasks(monday):
    """Fetch tasks completed in the week starting at *monday*."""
    sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
    # Asana search API: completed tasks in date range
    params = {
        "completed_since": monday.strftime("%Y-%m-%dT00:00:00Z"),
        "opt_fields": "name,created_at,completed_at,custom_fields,custom_fields.name,custom_fields.number_value",
    }
    tasks = asana_get(f"/projects/{PROJECT_GID}/tasks", params)
    # Filter to tasks completed within the week
    filtered = []
    for t in tasks:
        completed = fmt_date(t.get("completed_at"))
        if completed is None:
            continue
        # Ensure completed_at falls within [monday, sunday]
        completed_naive = completed.replace(tzinfo=None)
        if monday <= completed_naive <= sunday:
            filtered.append(t)
    return filtered


def extract_duration(task):
    """Return duration in minutes from custom field or estimate from timestamps."""
    # Check custom fields for "Duration (min)"
    for cf in task.get("custom_fields", []):
        if cf.get("name") == "Duration (min)" and cf.get("number_value") is not None:
            return cf["number_value"], "field"

    # Fallback: completed_at - created_at
    created = fmt_date(task.get("created_at"))
    completed = fmt_date(task.get("completed_at"))
    if created and completed:
        delta = completed - created
        minutes = delta.total_seconds() / 60
        return round(minutes, 1), "estimated"
    return None, "unknown"


def extract_project_name(task_name):
    """Extract [ProjectName] from task name, e.g. '... [foo-bar] ...' -> 'foo-bar'."""
    m = re.search(r"\[([^\]]+)\]", task_name)
    return m.group(1) if m else "Uncategorized"


def format_duration(minutes):
    """Format minutes as human-readable string."""
    if minutes is None:
        return "N/A"
    if minutes < 60:
        return f"{minutes:.0f}min"
    hours = minutes / 60
    return f"{hours:.1f}h ({minutes:.0f}min)"


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(tasks, monday):
    sunday = monday + timedelta(days=6)
    lines = []
    lines.append(f"# Weekly Summary: {monday.strftime('%Y-%m-%d')} ~ {sunday.strftime('%Y-%m-%d')}")
    lines.append("")

    if not tasks:
        lines.append("No completed tasks found for this week.")
        return "\n".join(lines)

    # Organize by day
    by_day = {}
    by_category = {}
    total_minutes = 0
    total_estimated = 0
    total_field = 0

    for t in tasks:
        completed = fmt_date(t["completed_at"]).replace(tzinfo=None)
        day_key = completed.strftime("%Y-%m-%d (%a)")
        duration, source = extract_duration(t)
        category = extract_project_name(t["name"])

        entry = {
            "name": t["name"],
            "duration": duration,
            "source": source,
            "created": fmt_date(t.get("created_at")),
            "completed": completed,
        }

        by_day.setdefault(day_key, []).append(entry)
        by_category.setdefault(category, []).append(entry)

        if duration is not None:
            total_minutes += duration
            if source == "field":
                total_field += duration
            else:
                total_estimated += duration

    # --- Daily breakdown ---
    lines.append("## Daily Breakdown")
    lines.append("")
    for day in sorted(by_day.keys()):
        entries = by_day[day]
        day_total = sum(e["duration"] or 0 for e in entries)
        lines.append(f"### {day}  ({format_duration(day_total)})")
        lines.append("")
        lines.append("| Task | Duration | Source |")
        lines.append("|------|----------|--------|")
        for e in entries:
            dur_str = format_duration(e["duration"]) if e["duration"] is not None else "N/A"
            lines.append(f"| {e['name']} | {dur_str} | {e['source']} |")
        lines.append("")

    # --- Category breakdown ---
    lines.append("## Category Breakdown")
    lines.append("")
    lines.append("| Category | Tasks | Total Duration |")
    lines.append("|----------|-------|----------------|")
    for cat in sorted(by_category.keys()):
        entries = by_category[cat]
        cat_total = sum(e["duration"] or 0 for e in entries)
        lines.append(f"| {cat} | {len(entries)} | {format_duration(cat_total)} |")
    lines.append("")

    # --- Weekly total ---
    lines.append("## Weekly Total")
    lines.append("")
    lines.append(f"- **Total tasks:** {len(tasks)}")
    lines.append(f"- **Total duration:** {format_duration(total_minutes)}")
    lines.append(f"  - From custom field: {format_duration(total_field)}")
    lines.append(f"  - Estimated (created->completed): {format_duration(total_estimated)}")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Asana AI Mission Control weekly summary")
    parser.add_argument(
        "--week",
        type=str,
        default=None,
        help="Monday of the target week (YYYY-MM-DD). Defaults to current week.",
    )
    args = parser.parse_args()

    monday = get_week_monday(args.week)
    print(f"Fetching tasks for week of {monday.strftime('%Y-%m-%d')}...", file=sys.stderr)

    tasks = fetch_completed_tasks(monday)
    print(f"Found {len(tasks)} completed tasks.", file=sys.stderr)

    report = generate_report(tasks, monday)
    print(report)


if __name__ == "__main__":
    main()
