# Function to calculate triangular number
def triangular(n):
    return (n * (n + 1)) // 2  # Formula: n(n+1)/2

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input
n = int(input("Give me a value of n: "))

# Print table header
print("\nCounting from j = 1 to", n, ":")
print(f"{'j':>5} {'tri':>5} {'factorial':>10}")  # Right-align header for formatting

# Loop to generate values
for j in range(1, n + 1):
    tri = triangular(j)
    fact = factorial(j)
    print(f"{j:5} {tri:5} {fact:10}")  # Formatting to match field width

