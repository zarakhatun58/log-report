# Access Log Report Task

An Apache-style access log is available at:

/app/access.log

Analyze the log and generate a JSON report at:

/app/report.json

The JSON object must contain exactly these fields:

- total_requests: the total number of log entries.
- unique_ips: the number of unique client IP addresses.
- top_path: the most frequently requested URL path.

Success criteria:

1. Create the output file at `/app/report.json`.
2. The output must be valid JSON.
3. `total_requests` must equal the number of log entries.
4. `unique_ips` must equal the number of distinct client IP addresses.
5. `top_path` must equal the most frequently requested URL path.

You have 320 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.