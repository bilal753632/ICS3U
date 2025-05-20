# Wordle Database Search Program
# Author: Bilal Siddiqui
# Date: May 18, 2025
# Student Number: 753632

# This program reads a Wordle data file and allows the user to search for
# the date a word appeared or which word appeared on a specific date.

def merge(day, month, year):
    """Converts 'day', 'month', 'year' into an integer of form YYYYMMDD."""
    month_nums = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    if month in month_nums:
        return int(f"{year}{month_nums[month]}{day}")
    else:
        return 0  # Invalid month

def isMatch(search_word, words, dates):
    """Search for the word in the words list and return the date it appeared."""
    search_word = search_word.upper()
    for i in range(len(words)):
        if words[i] == search_word:
            return dates[i]
    return 0  # Not found

# Step 1: Read data into arrays
dates = []
words = []

with open("wordle.dat", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 4:
            month, day, year, word = parts
            date_int = merge(day, month, year)
            dates.append(date_int)
            words.append(word)

# Step 2: Ask user for search type
print("Welcome to the Wordle Database!")
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").lower()

if choice == 'w':
    word = input("What word are you looking for? ").upper()
    result_date = isMatch(word, words, dates)
    if result_date != 0:
        print(f"The word {word} was the solution to the puzzle on {result_date}")
    else:
        print(f"{word} was not found in the database.")

elif choice == 'd':
    year = input("Enter the year: ")
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
    day = input("Enter the day: ")
    try:
        date_int = merge(day.zfill(2), month, year)
        if date_int < 20210619:
            print(f"{date_int} is too early. No wordles occurred before 20210619. Enter a later date.")
        elif date_int > 20240421:
            print(f"{date_int} is too recent. Our records only go as late as 20240421. Please enter an earlier date.")
        else:
            if date_int in dates:
                index = dates.index(date_int)
                print(f"The word entered on {date_int} was {words[index]}.")
            else:
                print(f"No Wordle found for the date {date_int}.")
    except:
        print("Invalid input. Please try again.")

else:
    print("Invalid choice. Please enter either 'w' or 'd'.")
