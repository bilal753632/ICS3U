# -----------------------------
# Name: Bilal Siddiqui
# Course Code: ICS3U
# Student Number: 753632
# Teacher: Mr. King
# Date: June 6, 2025
# Final Project: Credit Card Report
# -----------------------------

# This program reads credit card data from a file and finds all customers
# whose cards expire on or before June 2025. It outputs their info sorted by expiry date.

# Constants for expiry threshold
EXPIRY_CUTOFF_YEAR = 2025
EXPIRY_CUTOFF_MONTH = 6
EXPIRY_CUTOFF_DATE = EXPIRY_CUTOFF_YEAR * 100 + EXPIRY_CUTOFF_MONTH

# File names
INPUT_FILE = "data.dat"
OUTPUT_FILE = "output.txt"

# Lists to store data
first_names = []
last_names = []
cc_types = []
cc_numbers = []
exp_months = []
exp_years = []
exp_dates = []

# Read data from file
try:
    with open(INPUT_FILE, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 6:
                continue  # Skip malformed lines

            first_names.append(parts[0])
            last_names.append(parts[1])
            cc_types.append(parts[2])
            cc_numbers.append(parts[3])
            exp_month = int(parts[4])
            exp_year = int(parts[5])
            exp_months.append(exp_month)
            exp_years.append(exp_year)
            exp_dates.append(exp_year * 100 + exp_month)

except FileNotFoundError:
    print(f"❌ Error: File '{INPUT_FILE}' not found.")
    exit()

# Determine which customers need to update their cards
need_update = []

for i in range(len(exp_dates)):
    if exp_dates[i] <= EXPIRY_CUTOFF_DATE:
        need_update.append(i)

# Sort the list of indexes by expiry date using exchange sort
for i in range(len(need_update)):
    for j in range(i + 1, len(need_update)):
        if exp_dates[need_update[j]] < exp_dates[need_update[i]]:
            need_update[i], need_update[j] = need_update[j], need_update[i]

# Output results to file
with open(OUTPUT_FILE, "w") as out_file:
    for i in need_update:
        name = f"{first_names[i]} {last_names[i]}"
        ctype = cc_types[i]
        cnum = "#" + cc_numbers[i]
        exp = f"{exp_years[i]:04d}{exp_months[i]:02d}"
        status = "EXPIRED" if exp_dates[i] < EXPIRY_CUTOFF_DATE else "RENEW IMMEDIATELY"
        out_file.write(f"{name:<20} {ctype:<12} {cnum} {exp} {status}\n")

print("✅ Credit card report generated: output.txt")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
