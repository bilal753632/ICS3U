# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply by each number up to n
    return result

# Get user input
n = int(input("Enter a value for the upper limit, n: "))

# Print factorials from 0! to n!
print("\nFactorial Calculator:")
for i in range(n + 1):
    print(f"{i}! = {factorial(i)}")
