#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Function to print statistics."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def handle_interrupt(signal, frame):
    """Handle keyboard interrupt (CTRL + C) to print statistics."""
    print_statistics()
    sys.exit(0)

# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

# Read lines from stdin
for line in sys.stdin:
    try:
        # Parse line with expected format
        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract status code and file size
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update total file size
        total_file_size += file_size

        # Update status code count if it's one of the specified ones
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment line counter
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except (ValueError, IndexError):
        # Skip lines with incorrect format
        continue

# Print final statistics if input ends
print_statistics()
