import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

pattern = re.compile(
    r'"(?:GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+(\S+)'
)

with open("/app/access.log", "r") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        total += 1
        ips.add(line.split()[0])

        match = pattern.search(line)
        if match:
            paths[match.group(1)] += 1

report = {
    "total_requests": total,
    "unique_ips": len(ips),
    "top_path": paths.most_common(1)[0][0] if paths else None,
}

with open("/app/report.json", "w") as f:
    json.dump(report, f, indent=2)

print("Report written to /app/report.json")