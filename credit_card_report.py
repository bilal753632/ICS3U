# ---------------------------
# Name: Bilal Siddiqui
# Course: ICS3U
# Student Number: 753632
# Teacher: Mr. King
# Date: June 6, 2025
# Program: Credit Card Expiry Report
# ---------------------------

# This program reads credit card data from a file and writes a report of cards
# that are expired or need renewal (before or during June 2025).

# Constants
CURRENT_MONTH = 6
CURRENT_YEAR = 2025
CUTOFF_DATE = CURRENT_YEAR * 100 + CURRENT_MONTH  # 202506

# Arrays to hold data
first_names = []
last_names = []
card_types = []
card_numbers = []
expiries = []

try:
    with open("data.dat", "r") as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 6:
                continue  # skip malformed lines

            fname = parts[0].strip()
            lname = parts[1].strip()
            card_type = parts[2].strip()
            card_number = parts[3].strip()
            exp_month = int(parts[4].strip())
            exp_year = int(parts[5].strip())
            expiry = exp_year * 100 + exp_month  # Convert to sortable format

            if expiry <= CUTOFF_DATE:
                # Store valid expired/pending data
                first_names.append(fname)
                last_names.append(lname)
                card_types.append(card_type)
                card_numbers.append(card_number)
                expiries.append(expiry)

except FileNotFoundError:
    print("❌ ERROR: data.dat file not found.")
    exit()
except Exception as e:
    print("❌ ERROR while reading file:", e)
    exit()

# --- Exchange Sort (by expiry date) ---
n = len(expiries)
for i in range(n - 1):
    for j in range(i + 1, n):
        if expiries[j] < expiries[i]:
            # Swap everything
            expiries[i], expiries[j] = expiries[j], expiries[i]
            first_names[i], first_names[j] = first_names[j], first_names[i]
            last_names[i], last_names[j] = last_names[j], last_names[i]
            card_types[i], card_types[j] = card_types[j], card_types[i]
            card_numbers[i], card_numbers[j] = card_numbers[j], card_numbers[i]

# --- Write Output Report ---
try:
    with open("output.txt", "w") as output:
        for i in range(n):
            exp_str = str(expiries[i])
            year = exp_str[:4]
            month = exp_str[4:].zfill(2)
            status = "EXPIRED" if expiries[i] < CUTOFF_DATE else "RENEW IMMEDIATELY"
            output.write(f"{first_names[i]} {last_names[i]:<15} {card_types[i]:<12} #{card_numbers[i]} {year}{month} {status}\n")
    print("✅ Credit card report generated: output.txt")
except Exception as e:
    print("❌ ERROR writing output file:", e)
