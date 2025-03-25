print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if ch == "A":
    print("I prefer apples")
elif ch == "B":
    print("I prefer bananas")
elif ch == "C":
    print("I prefer cherries")
else:
    print("Invalid choice. Please select A, B, or C.")

# Marking system based on input number
grade = input("Enter a number from 1 to 100: ")

if grade.isdigit():  # Ensuring the input is a number
    grade = int(grade)
    if (grade >= 80) and (grade <= 100):
        print("Grade: A")
    elif (grade >= 70) and (grade <= 79):
        print("Grade: B")
    elif (grade >= 60) and (grade <= 69):
        print("Grade: C")
    elif (grade >= 50) and (grade <= 59):
        print("Grade: D")
    elif (grade >= 0) and (grade < 50):
        print("Grade: F")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
else:
    print("Invalid input. Please enter a valid number.")
