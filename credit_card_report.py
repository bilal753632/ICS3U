# Name: Bilal Siddiqui
# Student Number: 753632
# Course: ICS3U
# Teacher: Mr. King
# Assignment: Final Project – Credit Card Report
# Date: June 17, 2025

# This program reads customer credit card data, checks if any have expired or are about to expire,
# sorts them by expiry date, and outputs the result to a file.

# CONSTANTS
EXP_MONTH = 6
EXP_YEAR = 2025
EXP_DATE_CUTOFF = EXP_YEAR * 100 + EXP_MONTH

# ARRAYS
first_names = []
last_names = []
cc_types = []
cc_numbers = []
exp_months = []
exp_years = []
exp_dates = []  # computed as YYYYMM for easy comparison

# OUTPUT ARRAYS for expired cards
expired_first_names = []
expired_last_names = []
expired_cc_types = []
expired_cc_numbers = []
expired_dates = []

try:
    # Step 1: Read data
    with open("data.dat", "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 6:
                first_names.append(fields[0])
                last_names.append(fields[1])
                cc_types.append(fields[2])
                cc_numbers.append(fields[3])
                month = int(fields[4])
                year = int(fields[5])
                exp_months.append(month)
                exp_years.append(year)
                exp_dates.append(year * 100 + month)

    # Step 2: Filter expired or soon-to-expire cards
    for i in range(len(exp_dates)):
        if exp_dates[i] <= EXP_DATE_CUTOFF:
            expired_first_names.append(first_names[i])
            expired_last_names.append(last_names[i])
            expired_cc_types.append(cc_types[i])
            expired_cc_numbers.append(cc_numbers[i])
            expired_dates.append(exp_dates[i])

    # Step 3: Sort expired data using exchange sort (by expiry date)
    n = len(expired_dates)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if expired_dates[j] < expired_dates[i]:
                # Swap everything
                expired_dates[i], expired_dates[j] = expired_dates[j], expired_dates[i]
                expired_first_names[i], expired_first_names[j] = expired_first_names[j], expired_first_names[i]
                expired_last_names[i], expired_last_names[j] = expired_last_names[j], expired_last_names[i]
                expired_cc_types[i], expired_cc_types[j] = expired_cc_types[j], expired_cc_types[i]
                expired_cc_numbers[i], expired_cc_numbers[j] = expired_cc_numbers[j], expired_cc_numbers[i]

    # Step 4: Write results to output.txt
    with open("output.txt", "w") as out:
        for i in range(len(expired_dates)):
            year = expired_dates[i] // 100
            month = expired_dates[i] % 100
            expiry_str = f"{year}{month:02d}"
            status = "EXPIRED" if expired_dates[i] < EXP_DATE_CUTOFF else "RENEW IMMEDIATELY"
            out.write(f"{expired_first_names[i]} {expired_last_names[i]}: "
                      f"{expired_cc_types[i]:<13} #{expired_cc_numbers[i]} {expiry_str} {status}\n")

    print("✅ Credit card report generated: output.txt")

except FileNotFoundError:
    print("❌ Error: data.dat file not found. Please make sure it exists in the same folder.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
