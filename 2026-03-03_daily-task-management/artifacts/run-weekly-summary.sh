#!/bin/bash
export ASANA_PAT="$(security find-generic-password -s 'asana-pat' -w 2>/dev/null || echo $ASANA_PAT)"
python3 "$(dirname "$0")/asana-weekly-summary.py" "$@"
