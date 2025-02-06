year = input("What year were you born?:")
age = input("How old are you?:")
year = int(year)
age = int(age)
year2 = year * 2 + 5
year3 = year2 * 50 + age
year4 = year3 - 250
year5 = year4 / 100
print("When", year, "is doubled, added 5, multiplied by 50, added", end=" ")
print(age," subtracted by 250 and added by 100", "the result is:", year5)
