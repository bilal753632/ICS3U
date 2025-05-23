# Part 1: Even or Odd?
print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

# Ask the user to enter two whole numbers
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

# If either number is even, the product will be even
if (num1 % 2 == 0) or (num2 % 2 == 0):
    print(f"The product {num1} x {num2} will be an even number.")
# If both numbers are odd, the product will be odd
else:
    print(f"The product {num1} x {num2} will be an odd number.")

# Part 2: Cube Inner Diagonal Calculation
print("\nI will find the cube's inner diagonal for any edge length!")

# Ask the user to enter the length of one edge of the cube
edge_length = float(input("Please enter the edge length of your cube: "))

# Use a math formula to find the diagonal that goes through the middle of the cube
inner_diagonal = (3 * (edge_length ** 2)) ** 0.5

# Show the result, rounded to 2 decimal places
print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {round(inner_diagonal, 2)}")

# Part 3: Making Change in Coins
print("\nLet's calculate the minimum number of coins for your change!")

# Ask the user to enter an amount in cents
cents = int(input("Please enter the amount of change in cents: "))

# If it's more than a dollar (100 cents), take out the dollar part first
if cents >= 100:
    dollars = cents // 100       # Find how many dollars
    cents = cents % 100          # Find out what’s left after taking out dollars
    print(f"You entered more than $1.00. The dollar value of {dollars} was subtracted, leaving {cents} cents.")

# Figure out how many quarters (25 cents) fit in the remaining cents
quarters = cents // 25
cents = cents % 25

# Then how many dimes (10 cents)
dimes = cents // 10
cents = cents % 10

# Then how many nickels (5 cents)
nickels = cents // 5
cents = cents % 5

# What’s left are pennies (1 cent each)
pennies = cents

# Print the result, only showing coins that are actually used
print("Your change can be given as:")
if quarters > 0:
    print(f"{quarters} quarter(s)")
if dimes > 0:
    print(f"{dimes} dime(s)")
if nickels > 0:
    print(f"{nickels} nickel(s)")
if pennies > 0:
    print(f"{pennies} penny/pennies")
