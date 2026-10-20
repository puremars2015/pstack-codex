"""Append a decision to a local TSV without shell quoting or platform dependencies."""
import argparse, csv, datetime
from pathlib import Path
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--path', required=True)
for key in ('decision', 'evidence', 'alternative', 'status'):
    p.add_argument('--' + key, required=key in ('decision', 'evidence'), default='')
a = p.parse_args()
target = Path(a.path)
target.parent.mkdir(parents=True, exist_ok=True)
fields = ['time_utc', 'decision', 'evidence', 'alternative', 'status']
exists = target.exists() and target.stat().st_size > 0
if exists:
    with target.open(newline='', encoding='utf-8') as f:
        if next(csv.reader(f, delimiter='\t'), None) != fields:
            p.error('Existing TSV has an incompatible header; file was not changed.')
with target.open('a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\t')
    if not exists:
        w.writerow(fields)
    # Avoid spreadsheet formula interpretation when this TSV is opened later.
    def cell(s):
        return "'" + s if s.lstrip().startswith(('=', '+', '-', '@')) else s
    w.writerow([datetime.datetime.now(datetime.timezone.utc).isoformat()] +
               [cell(getattr(a, k)) for k in fields[1:]])
print(str(target.resolve()))
