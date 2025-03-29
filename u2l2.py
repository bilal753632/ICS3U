# Function to determine suffix (st, nd, rd, th)
def get_suffix(n):
    if n == 1:
        return "st"
    elif n == 2:
        return "nd"
    elif n == 3:
        return "rd"
    else:
        return "th"

# Loop to calculate triangular numbers
for n in range(1, 7):  # From 1 to 6
    triangular_number = (n * (n + 1)) // 2
    suffix = get_suffix(n)
    print(f"The {n}{suffix} triangular number is {triangular_number}")
