import sys
import os

# Function to parse a single log line
def parse_log_line(line):
    parts = line.strip().split(" ", 3)  # Split line into date, time, level, and message
    if len(parts) < 4:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

# Function to load logs from a file
def load_logs(file_path):
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    return logs

# Function to filter logs by level
def filter_logs_by_level(logs, level):
    return [log for log in logs if log["level"].lower() == level.lower()]

# Function to count logs by level
def count_logs_by_level(logs):
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

# Function to display log counts
def display_log_counts(counts):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

# Main script logic
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_log_file> [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    # Load logs from file
    logs = load_logs(log_file_path)

    # Count logs by level
    log_counts = count_logs_by_level(logs)

    # Display log counts
    display_log_counts(log_counts)

    # If a specific log level is provided, display its details
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()