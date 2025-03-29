score = input("Enter a score from 1 to 100: ")

# Convert input to integer
if score.isdigit():  # Ensure input is a number
    score = int(score)
    
    if (score >= 80) and (score <= 100):
        print("Grade: A")
    elif (score >= 70) and (score <= 79):
        print("Grade: B")
    elif (score >= 60) and (score <= 69):
        print("Grade: C")
    elif (score >= 50) and (score <= 59):
        print("Grade: D")
    elif (score < 50) and (score >= 1):
        print("Grade: F")
    else:
        print("Invalid score. Enter a number between 1 and 100.")
else:
    print("Invalid input. Please enter a number.")
