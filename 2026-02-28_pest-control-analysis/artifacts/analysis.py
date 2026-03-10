#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pest Control Effectiveness Analysis
Sydney Apartment - Post Professional Treatment (2/10)
"""

import numpy as np
from datetime import datetime, timedelta

# Data structure: (date, dead_count, live_count, notes)
data = [
    ("2/11", 2, 0, "2 dead adults"),
    ("2/12", 0, 0, ""),
    ("2/13", 0, 2, "2 live juveniles + kitchen sealed"),
    ("2/14", 0, 2, "2 live juveniles"),
    ("2/15", 1, 1, "1 dead + 1 live juvenile + bathroom sealed"),
    ("2/16", 0, 0, ""),
    ("2/17", 3, 0, "3 dead juveniles"),
    ("2/18", 0, 2, "2 live adults + frass in dishwasher + cardboard removed + 5 baits"),
    ("2/19", 0, 1, "1 live juvenile"),
    ("2/20", 3, 1, "3 dead + 1 live juvenile"),
    ("2/21", 3, 0, "2 dead (morning) + 1 dead (afternoon) + 3 baits added"),
    ("2/22", 1, 0, "1 dead (morning) + 1 bait added"),
    ("2/23", 0, 0, ""),
    ("2/24", 0, 0, ""),
    ("2/25", 1, 0, "1 dead juvenile"),
    ("2/26", 0, 0, "heavy rain started"),
    ("2/27", 2, 0, "2 dead juveniles (noon) + heavy rain + metal frame installed"),
    ("2/28", 2, 1, "1 dead (evening) + 1 live (ceiling) + 1 dead (night) + 2 baits added"),
]

# Parse data
dates = []
dead_counts = []
live_counts = []
total_counts = []

for entry in data:
    date_str, dead, live, note = entry
    dates.append(date_str)
    dead_counts.append(dead)
    live_counts.append(live)
    total_counts.append(dead + live)

# Calculate weekly averages
week1_data = total_counts[0:7]   # 2/11-2/17 (day 1-7 post treatment)
week2_data = total_counts[7:14]  # 2/18-2/24 (day 8-14)
week3_data = total_counts[14:18] # 2/25-2/28 (day 15-18)

week1_avg = np.mean(week1_data)
week2_avg = np.mean(week2_data)
week3_avg = np.mean(week3_data)

print("=" * 80)
print("害虫駆除効果分析レポート")
print("=" * 80)
print()

# Q1: Weekly averages
print("【1. 週別平均値とトレンド】")
print(f"Week 1 (2/11-2/17): 平均 {week1_avg:.2f} 件/日")
print(f"  データ: {week1_data}")
print(f"  合計: {sum(week1_data)} 件")
print()
print(f"Week 2 (2/18-2/24): 平均 {week2_avg:.2f} 件/日")
print(f"  データ: {week2_data}")
print(f"  合計: {sum(week2_data)} 件")
print()
print(f"Week 3 (2/25-2/28): 平均 {week3_avg:.2f} 件/日")
print(f"  データ: {week3_data}")
print(f"  合計: {sum(week3_data)} 件")
print()
print(f"トレンド: Week 1 → Week 2 = {((week2_avg - week1_avg) / week1_avg * 100):+.1f}%")
print(f"トレンド: Week 2 → Week 3 = {((week3_avg - week2_avg) / week2_avg * 100):+.1f}%")
print()

# Q2: Is 2/28 an outlier?
print("【2. 2/28の統計的評価】")
recent_baseline = total_counts[14:17]  # 2/25, 2/26, 2/27
feb28_value = total_counts[17]  # 2/28

print(f"直近ベースライン (2/25-2/27): {recent_baseline}")
print(f"ベースライン平均: {np.mean(recent_baseline):.2f} 件/日")
print(f"ベースライン標準偏差: {np.std(recent_baseline, ddof=1):.2f}")
print(f"2/28の値: {feb28_value} 件")
print()

# Z-score calculation
if np.std(recent_baseline, ddof=1) > 0:
    z_score = (feb28_value - np.mean(recent_baseline)) / np.std(recent_baseline, ddof=1)
    print(f"Z-score: {z_score:.2f}")
    if abs(z_score) < 1.0:
        print("評価: 統計的に正常範囲内（|Z| < 1.0）")
    elif abs(z_score) < 2.0:
        print("評価: 軽度の変動（1.0 ≤ |Z| < 2.0）")
    else:
        print("評価: 統計的外れ値の可能性（|Z| ≥ 2.0）")
else:
    print("評価: ベースラインの分散が小さすぎるため、Z-scoreは計算不可")
    print(f"2/28の値 ({feb28_value}) は直近平均 ({np.mean(recent_baseline):.2f}) と比較して {feb28_value - np.mean(recent_baseline):+.0f} 件の差")

print()

# Q3: Dead vs Live ratio
print("【3. 死骸 vs 生存個体の比率（全期間）】")
total_dead = sum(dead_counts)
total_live = sum(live_counts)
total_all = total_dead + total_live

print(f"死骸合計: {total_dead} 件 ({total_dead/total_all*100:.1f}%)")
print(f"生存個体合計: {total_live} 件 ({total_live/total_all*100:.1f}%)")
print()

# Recent period (last 7 days)
recent_dead = sum(dead_counts[11:18])  # 2/22-2/28
recent_live = sum(live_counts[11:18])
recent_total = recent_dead + recent_live

print(f"【直近7日間 (2/22-2/28) の比率】")
print(f"死骸: {recent_dead} 件 ({recent_dead/recent_total*100:.1f}%)")
print(f"生存個体: {recent_live} 件 ({recent_live/recent_total*100:.1f}%)")
print()

# Q4: Trend analysis - converging to zero?
print("【4. ゼロ収束性の判定】")

# Linear regression on total counts (manual calculation)
days = np.arange(len(total_counts))
x_mean = np.mean(days)
y_mean = np.mean(total_counts)
numerator = np.sum((days - x_mean) * (total_counts - y_mean))
denominator = np.sum((days - x_mean) ** 2)
slope = numerator / denominator
intercept = y_mean - slope * x_mean
# R-squared
y_pred = intercept + slope * days
ss_tot = np.sum((total_counts - y_mean) ** 2)
ss_res = np.sum((total_counts - y_pred) ** 2)
r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0

print(f"線形回帰分析:")
print(f"  傾き: {slope:.4f} 件/日")
print(f"  切片: {intercept:.4f}")
print(f"  R²: {r_squared:.4f}")
print()

if slope < -0.05:
    print(f"トレンド判定: 減少傾向（傾き = {slope:.4f} < -0.05）")
    if abs(slope) > 0.1:
        print("  → 明確な減少トレンド")
    else:
        print("  → 緩やかな減少トレンド")
elif slope > 0.05:
    print(f"トレンド判定: 増加傾向（傾き = {slope:.4f} > 0.05）⚠️")
    print("  → 警戒が必要")
else:
    print(f"トレンド判定: 横ばい（-0.05 ≤ 傾き = {slope:.4f} ≤ 0.05）")
    print("  → 現状維持")

print()

# Recent 7-day trend
recent_days = np.arange(7)
recent_data = total_counts[11:18]
recent_x_mean = np.mean(recent_days)
recent_y_mean = np.mean(recent_data)
recent_numerator = np.sum((recent_days - recent_x_mean) * (recent_data - recent_y_mean))
recent_denominator = np.sum((recent_days - recent_x_mean) ** 2)
recent_slope = recent_numerator / recent_denominator
recent_intercept = recent_y_mean - recent_slope * recent_x_mean
recent_y_pred = recent_intercept + recent_slope * recent_days
recent_ss_tot = np.sum((recent_data - recent_y_mean) ** 2)
recent_ss_res = np.sum((recent_data - recent_y_pred) ** 2)
recent_r_squared = 1 - (recent_ss_res / recent_ss_tot) if recent_ss_tot > 0 else 0
print(f"直近7日間のトレンド (2/22-2/28):")
print(f"  傾き: {recent_slope:.4f} 件/日")
print(f"  R²: {recent_r_squared:.4f}")
print()

# Zero convergence estimate
if slope < 0:
    days_to_zero = -intercept / slope
    print(f"ゼロ到達予測: 約 {days_to_zero:.1f} 日後（線形モデル）")
    if days_to_zero < 0:
        print("  → すでにゼロ水準に近い")
    elif days_to_zero < 7:
        print("  → 1週間以内に収束予測")
    elif days_to_zero < 14:
        print("  → 2週間以内に収束予測")
    else:
        print("  → 収束まで時間がかかる可能性")
else:
    print("ゼロ到達予測: トレンドが減少していないため予測不可")

print()

# Q5: Emergency assessment - "Second wave" claim
print("【5. 「緊急事態」「第二波」の主張に対する検証】")
print()
print("Geminiの主張: 2/28は緊急事態であり、第二波の兆候")
print()

# Evidence analysis
print("データに基づく反証:")
print()

# 1. Compare to peak
peak_value = max(total_counts)
peak_date = dates[total_counts.index(peak_value)]
print(f"1. ピーク値との比較")
print(f"   全期間最大: {peak_value} 件 ({peak_date})")
print(f"   2/28の値: {feb28_value} 件")
print(f"   → 2/28はピークの {feb28_value/peak_value*100:.1f}% のみ")
print()

# 2. Week 1 comparison
week1_max = max(week1_data)
print(f"2. Week 1最大値との比較")
print(f"   Week 1最大: {week1_max} 件")
print(f"   2/28の値: {feb28_value} 件")
print(f"   → Week 1の {feb28_value/week1_max*100:.1f}%")
print()

# 3. Recent zero days
zero_days = [i for i, count in enumerate(total_counts[14:18]) if count == 0]
print(f"3. Week 3のゼロ発見日")
print(f"   2/26: {total_counts[15]} 件 (ゼロ)")
print(f"   Week 3でのゼロ日数: {len(zero_days)} 日 / 4 日")
print()

# 4. Live specimen trend
live_recent_7d = live_counts[11:18]
print(f"4. 生存個体の推移（直近7日）")
print(f"   データ: {live_recent_7d}")
print(f"   合計: {sum(live_recent_7d)} 件")
print(f"   平均: {np.mean(live_recent_7d):.2f} 件/日")
print()

# 5. Pattern analysis
print(f"5. パターン分析")
consecutive_zeros = []
current_streak = 0
for count in total_counts[14:]:
    if count == 0:
        current_streak += 1
    else:
        if current_streak > 0:
            consecutive_zeros.append(current_streak)
        current_streak = 0
if current_streak > 0:
    consecutive_zeros.append(current_streak)

print(f"   Week 3の連続ゼロ記録: {consecutive_zeros}")
print(f"   最長連続ゼロ: {max(consecutive_zeros) if consecutive_zeros else 0} 日")
print()

# Final verdict
print("【総合判定】")
print()
print("「緊急事態」の評価:")
if feb28_value <= week3_avg:
    print(f"  ❌ 否定: 2/28 ({feb28_value}件) は Week 3 平均 ({week3_avg:.2f}件) 以下")
else:
    print(f"  ⚠️  微増: 2/28 ({feb28_value}件) は Week 3 平均 ({week3_avg:.2f}件) をやや上回る")

print()
print("「第二波」の評価:")

# Check if there's a clear trough followed by sustained increase
trough_indices = [i for i in range(14, 17) if total_counts[i] == 0]
if trough_indices and feb28_value > 0:
    # Check if 2/28 represents a sustained increase
    if feb28_value > week3_avg * 1.5:
        print(f"  ⚠️  警戒: ゼロ日の後に {feb28_value} 件まで増加")
    else:
        print(f"  ❌ 否定: 単発の変動の範囲内（週平均 {week3_avg:.2f} の範囲）")
else:
    print(f"  ❌ 否定: 明確な谷と再増加のパターンは見られない")

print()

# Statistical significance of any increase
if len(week3_data) >= 3:
    week3_first_half = week3_data[:2]
    week3_second_half = week3_data[2:]
    print(f"Week 3 前半 (2/25-2/26): 平均 {np.mean(week3_first_half):.2f}")
    print(f"Week 3 後半 (2/27-2/28): 平均 {np.mean(week3_second_half):.2f}")
    change_pct = (np.mean(week3_second_half) - np.mean(week3_first_half)) / (np.mean(week3_first_half) + 0.01) * 100
    print(f"変化率: {change_pct:+.1f}%")

print()
print("=" * 80)
print("結論:")
print("=" * 80)
print()

# Final conclusion with numbers
overall_trend = (week3_avg - week1_avg) / week1_avg * 100
print(f"全体トレンド: Week 1 → Week 3 で {overall_trend:+.1f}% 変化")
print(f"死骸比率: {recent_dead/recent_total*100:.1f}% (直近7日)")
print(f"傾き: {slope:.4f} 件/日（全期間）, {recent_slope:.4f} 件/日（直近7日）")
print()

if overall_trend < -30 and recent_dead/recent_total > 0.7 and recent_slope <= 0:
    print("✅ 駆除は効果的に機能している")
    print("   - 週平均が30%以上減少")
    print("   - 死骸比率70%以上（薬剤効果継続）")
    print("   - 直近トレンドは横ばいまたは減少")
    print()
    print("「緊急事態」「第二波」の主張は:")
    print("   ❌ データに基づかない過剰反応")
    print()
    if feb28_value > 0:
        print("2/28の発見は:")
        print("   - 散発的な残存個体の可能性が高い")
        print("   - 継続的なモニタリングは必要だが、緊急対応は不要")
else:
    print("⚠️  慎重な観察が必要")
    print("   追加データで判断を継続")

print()
print("=" * 80)

print()
print("=" * 80)
print("分析完了")
