import random

# Generate a random number between 1 and 100 (inclusive)
a = random.randrange(1, 101)

# Introduction and instructions
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
print("You have a maximum of six (6) tries.")

# Initialize guess counter and user's guess variable
c = 1
x = 0

# Loop runs while the user still has guesses left and hasn't guessed the number
while c <= 6 and x != a:
    try:
        # Prompt the user to make a guess
        x = int(input(f"Guess #{c}: "))
    except ValueError:
        # Handle non-integer input gracefully
        print("Please enter a valid integer.")
        continue  # Skip the rest of the loop and prompt again

    # Provide a hint if the guess is too low
    if x < a:
        print("Higher")
    # Provide a hint if the guess is too high
    elif x > a:
        print("Lower")
    # Congratulate the user if they guessed correctly
    else:
        print("You guessed right!")
        break  # Exit the loop since the correct number was guessed

    # Increment the guess counter
    c += 1

# If the loop ends without a correct guess, reveal the answer
if x != a:
    print(f"You are out of guesses! The answer was {a}. Better luck next time!")

