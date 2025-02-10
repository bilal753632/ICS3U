import math

x = int(input("Please input a whole number between 1 and 20: "))

if 1 <= x <= 20:
    y = int(input("Please input another whole number between 1 and 20: "))
    
    if 1 <= y <= 20:
        print("Now deciding if", y, "is a factor of", x, "...")
        if y != 0:
            rem = x % y
            if rem == 0:
                print("Yes!", y, "is a factor of", x)
        else:
            print("You cannot enter zero. A factor could not be determined.")
    else:
        print("The second number must be between 1 and 20.")
else:
    print("The first number must be between 1 and 20.")
