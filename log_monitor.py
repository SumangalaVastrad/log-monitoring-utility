filename = input("Enter log file name: ")

error_count = 0
warning_count = 0
info_count = 0
critical_count = 0

try:
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        if "CRITICAL" in line:
            critical_count = critical_count + 1
        elif "ERROR" in line:
            error_count = error_count + 1
        elif "WARNING" in line:
            warning_count = warning_count + 1
        elif "INFO" in line:
            info_count = info_count + 1
    file.close()

    print("Errors:", error_count)
    print("Warnings:", warning_count)
    print("Info:", info_count)
    print("Critical:", critical_count)

    report = open("report.txt", "w")
    report.write("LOG SUMMARY REPORT\n")
    report.write("Errors: " + str(error_count) + "\n")
    report.write("Warnings: " + str(warning_count) + "\n")
    report.write("Info: " + str(info_count) + "\n")
    report.write("Critical: " + str(critical_count) + "\n")
    report.close()
    print("Report saved to report.txt")

except FileNotFoundError:
    print("Log file not found")