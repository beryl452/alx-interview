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
        # print(f"...\n..{line}\n..{data}\n...")
        status_code = data[-2]
        file_size = data[-1]
        return (status_code, file_size)
    except:
        return (None, None)

def print_stats(total_file_size, status_code_size):
    """Prints the statistics.
    Args:
        total_file_size (int): The total file size.
        status_code_size (dict): The status code sizes.
    """
    print('File size: {}'.format(total_file_size))
    for status_code, size in sorted(status_code_size.items()):
        print('{}: {}'.format(status_code, size))

def main():
    """Parses log lines from standard input.
    """
    line_number = 0
    total_file_size = 0
    status_code_size = {}

    try:
        while True:
            line = sys.stdin.readline()
            line_number += 1
            status_code, file_size = extract_data(line)
            total_file_size += int(file_size)
            if status_code in status_code_size:
                status_code_size[status_code] += 1
            else:
                status_code_size[status_code] = 1
            if (line_number % 10 == 0):
                print_stats(total_file_size, status_code_size)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_file_size, status_code_size)

if __name__ == '__main__':
    main()
