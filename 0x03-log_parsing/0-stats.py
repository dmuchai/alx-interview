#!/usr/bin/python3
"""
A script that reads log data from standard input, line by line,
computes metrics (total file size and count of lines by status code),
and prints these statistics after every 10 successfully processed lines
and/or upon a keyboard interruption (CTRL + C).

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Lines not matching this format or containing invalid data for status code/file size are skipped.
Status codes are printed in ascending order. Only status codes that have appeared are printed.
"""
import sys
import re


def print_metrics(total_file_size, status_codes_summary):
    """
    Prints the accumulated total file size and the counts for each
    HTTP status code.

    Args:
        total_file_size (int): The cumulative sum of file sizes.
        status_codes_summary (dict): A dictionary where keys are status codes (int)
                                     and values are their counts (int).
    """
    print(f"File size: {total_file_size}")
    # Print status codes in ascending order.
    # Only print status codes that have appeared (i.e., are keys in the dict
    # and implicitly have a count > 0).
    for code in sorted(status_codes_summary.keys()):
        print(f"{code}: {status_codes_summary[code]}")


if __name__ == "__main__":
    # Regular expression to parse the log line format.
    # Example line: 123.45.67.89 - [2023-10-27 10:00:00.000000] "GET /projects/260 HTTP/1.1" 200 1024
    log_entry_pattern = re.compile(
        r'^(?P<ip>(?:\d{1,3}\.){3}\d{1,3}) - '  # IP Address
        r'\[(?P<date>.*?)\] '                   # Date (any characters within brackets)
        r'"GET /projects/260 HTTP/1\.1" '       # Specific GET request string
        r'(?P<status_code_str>\S+) '            # Status code (captured as string)
        r'(?P<file_size_str>\S+)$'              # File size (captured as string)
    )

    # Set of valid HTTP status codes to track, as specified.
    VALID_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

    # Initialize metrics
    cumulative_file_size = 0
    # Dictionary to store counts of status codes: {<int_status_code>: count}
    status_code_counts = {}
    # Counter for lines that have been successfully parsed and processed
    valid_lines_processed_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()  # Remove leading/trailing whitespace

            match = log_entry_pattern.fullmatch(line)

            if not match:
                # If the line does not match the expected base format, skip it.
                continue

            log_data = match.groupdict()
            status_code_str = log_data.get('status_code_str')
            file_size_str = log_data.get('file_size_str')

            # Attempt to convert status code and file size to integers.
            # If conversion fails, the line is considered malformed for these fields.
            try:
                status_code = int(status_code_str)
                file_size = int(file_size_str)
            except ValueError:
                # Skip lines where status code or file size are not valid integers.
                continue

            # Check if the parsed status code is one of the recognized valid codes.
            if status_code not in VALID_STATUS_CODES:
                # If status code is valid integer but not in the defined list,
                # skip this line for metrics calculation as per problem implication
                # (only specified status codes are counted).
                continue

            # If all checks pass (format, integer conversion, valid status code),
            # update the metrics.
            cumulative_file_size += file_size
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
            valid_lines_processed_count += 1

            # After every 10 validly processed lines, print the current statistics.
            if valid_lines_processed_count > 0 and valid_lines_processed_count % 10 == 0:
                print_metrics(cumulative_file_size, status_code_counts)

    except KeyboardInterrupt:
        # On keyboard interruption (CTRL + C), print the final current statistics.
        print_metrics(cumulative_file_size, status_code_counts)
        # Re-raise the KeyboardInterrupt to allow the script to terminate
        # and display the traceback, matching the example output behavior.
        raise
    
    # Per the problem description ("After every 10 lines and/or a keyboard interruption"),
    # there is no explicit requirement to print stats on normal EOF if the last batch
    # of processed lines was less than 10 and no interruption occurred.
    # The current structure adheres to this.
