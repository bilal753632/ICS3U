print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

# Step 1: Input two numbers
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

# Step 2: Check if product will be even or odd
if num1 % 2 == 0 or num2 % 2 == 0:
    print(f"The product {num1} x {num2} will be an even number.")
else:
    print(f"The product {num1} x {num2} will be an odd number.")

print("\nI will find the cube's inner diagonal for any edge length!")

# Step 3: Input edge length of the cube
edge_length = float(input("Please enter the edge length of your cube: "))

# Step 4: Calculate the diagonal (diagonal formula: edge_length * sqrt(3))
if edge_length > 0:
    diagonal = edge_length * 1.732  # Approximation for sqrt(3)
    diagonal = round(diagonal, 2)
    print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {diagonal}")
else:
    print("Invalid input for edge length.")

print("\nLet's make change using the fewest coins possible!")

# Step 5: Input amount in cents
cents = int(input("Please enter the amount of change in cents: "))

# Step 6: Determine the coin distribution
if cents >= 100:
    cents = cents % 100  # Ensure amount is less than $1.00

quarters = 0
dimes = 0
nickels = 0
pennies = 0

if cents >= 25:
    quarters = cents // 25
    cents = cents % 25

if cents >= 10:
    dimes = cents // 10
    cents = cents % 10

if cents >= 5:
    nickels = cents // 5
    cents = cents % 5

pennies = cents

# Step 7: Prepare output message
output = ""
if quarters > 0:
    output += f"{quarters} quarter{'s' if quarters > 1 else ''}, "
if dimes > 0:
    output += f"{dimes}
