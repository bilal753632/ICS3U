import math

print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

if num1 % 2 == 0 or num2 % 2 == 0:
    print(f"The product {num1} x {num2} will be an even number.")
else:
    print(f"The product {num1} x {num2} will be an odd number.")

print("\nI will find the cube's inner diagonal for any edge length!")
edge_length = float(input("Please enter the edge length of your cube: "))
diagonal = round(edge_length * math.sqrt(3), 2)
print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {diagonal}")

print("\nLet's make change using the fewest coins possible!")
cents = int(input("Please enter the amount of change in cents: "))

if cents >= 100:
    cents = cents % 100  # Ensure amount is less than $1.00

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

output = ""
if quarters > 0:
    output += f"{quarters} quarter{'s' if quarters > 1 else ''}, "
if dimes > 0:
    output += f"{dimes} dime{'s' if dimes > 1 else ''}, "
if nickels > 0:
    output += f"{nickels} nickel{'s' if nickels > 1 else ''}, "
if pennies > 0:
    output += f"{pennies} penn{'ies' if pennies > 1 else 'y'}, "

print(output.rstrip(', ') + ".")
