print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

# Part 1: Even or Odd?
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

if (num1 % 2 == 0) or (num2 % 2 == 0):
    print(f"The product {num1} x {num2} will be an even number.")
else:
    print(f"The product {num1} x {num2} will be an odd number.")

# Part 2: Cube Inner Diagonal Calculation
print("\nI will find the cube's inner diagonal for any edge length!")
edge_length = float(input("Please enter the edge length of your cube: "))
inner_diagonal = (3 * (edge_length ** 2)) ** 0.5
print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {round(inner_diagonal, 2)}")

# Part 3: Making Change in Coins
print("\nLet's calculate the minimum number of coins for your change!")
cents = int(input("Please enter the amount of change in cents: "))

if cents >= 100:
    dollars = cents // 100
    cents = cents % 100
    print(f"You entered more than $1.00. The dollar value of {dollars} was subtracted, leaving {cents} cents.")

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

print("Your change can be given as:")
if quarters > 0:
    print(f"{quarters} quarter(s)")
if dimes > 0:
    print(f"{dimes} dime(s)")
if nickels > 0:
    print(f"{nickels} nickel(s)")
if pennies > 0:
    print(f"{pennies} penny/pennies")
