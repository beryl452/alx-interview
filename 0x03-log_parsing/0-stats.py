#!/usr/bin/python3
"""A script for parsing HTTP request logs.
"""
import sys

def extract_data(line):
    """Extracts the data from a log line.
    Args:
        line (str): The log line.
    Returns:
        tuple: The data extracted from the log line.
    """
    try:
        data = line.split()
        if len(data) < 9:
            return (None, None)
        status_code = data[7]
        file_size = data[8]
        return (status_code, file_size)
    except (IndexError, ValueError):
        return (None, None)

def print_stats(total_file_size, status_code_count):
    """Prints the statistics.
    Args:
        total_file_size (int): The total file size.
        status_code_count (dict): The status code counts.
    """
    print('File size: {}'.format(total_file_size), flush=True)
    for status_code, count in sorted(status_code_count.items()):
        print('{}: {}'.format(status_code, count), flush=True)

def main():
    """Parses log lines from standard input.
    """
    line_number = 0
    total_file_size = 0
    status_code_count = {}

    try:
        while True:
            line = sys.stdin.readline()
            line_number += 1
            status_code, file_size = extract_data(line)
            if status_code.isdigit() and file_size.isdigit():
                status_code = int(status_code)
                file_size = int(file_size)
                total_file_size += file_size
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                else:
                    status_code_count[status_code] = 1
            if (line_number % 10 == 0):
                print_stats(total_file_size, status_code_count)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_file_size, status_code_count)

if __name__ == '__main__':
    main()
