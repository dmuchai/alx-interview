#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
total_size = 0
status_counts = defaultdict(int)
line_counter = 0

# List of valid status codes (as strings)
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Regex pattern to match the valid log line
log_pattern = re.compile(
    r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

def print_stats():
    """
    Print current statistics: total file size and status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code, file_size_str = match.groups()
            if status_code in valid_status_codes:
                status_counts[status_code] += 1
            try:
                total_size += int(file_size_str)
            except ValueError:
                pass  # Ignore bad file sizes

        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # On Ctrl+C, print the stats before exiting
    print_stats()
    raise

# Print final stats if not already done
print_stats()
