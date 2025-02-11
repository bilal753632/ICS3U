x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)

if 1 <= x <= 20:

    if 1 <= y <= 20:
        print("Now deciding if", y, "is a factor of", x)

        if x % y == 0:
            print("Yes!", y, "is a factor of", x)
        else:
            print("No!", y, "is not a factor of", x)
    else:
        print("Error: The second number must be between 1 and 20")
else:
    print("Error: The first number must be between 1 and 20")
