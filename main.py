# Log File Analyzer - Starter Code
# Run: python main.py

def read_log_file(filename):
    """Read all lines from the log file"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def analyze_logs(lines):
    """Count total lines, errors, and track error types"""
    total_lines = len(lines)
    error_lines = []
    error_count = {}

    for line in lines:
        line = line.strip()
        if "ERROR" in line or "FAILED" in line:
            error_lines.append(line)
            # Get the error type, e.g. TIMEOUT, 404, etc
            words = line.split()
            for word in words:
                if word.isupper() and len(word) > 3:
                    error_count[word] = error_count.get(word, 0) + 1

    return total_lines, len(error_lines), error_count

def print_report(total_lines, error_count_total, error_count):
    """Print summary report"""
    print("\n========== LOG ANALYSIS REPORT ==========")
    print(f"Total lines processed: {total_lines}")
    print(f"Total errors found: {error_count_total}")

    if error_count:
        print("\nTop error types:")
        # Sort errors by count, show top 3
        sorted_errors = sorted(error_count.items(), key=lambda x: x[1], reverse=True)
        for i, (error_type, count) in enumerate(sorted_errors[:3], 1):
            print(f" {i}. {error_type}: {count} times")
    else:
        print("No errors found. Nice!")
    print("========================================\n")

def save_report(filename, total_lines, error_count_total, error_count):
    """Save report to a new file"""
    with open("report.txt", "w") as f:
        f.write("LOG ANALYSIS REPORT\n")
        f.write(f"Total lines: {total_lines}\n")
        f.write(f"Total errors: {error_count_total}\n")
        f.write("Error breakdown:\n")
        for error_type, count in error_count.items():
            f.write(f"{error_type}: {count}\n")
    print("Report saved to report.txt")

def main():
    print("Log File Analyzer")
    filename = input("Enter log file name: ")

    lines = read_log_file(filename)
    if not lines:
        return

    total_lines, error_count_total, error_count = analyze_logs(lines)
    print_report(total_lines, error_count_total, error_count)

    save = input("Save report to file? y/n: ").lower()
    if save == "y":
        save_report(filename, total_lines, error_count_total, error_count)

if __name__ == "__main__":
    main()