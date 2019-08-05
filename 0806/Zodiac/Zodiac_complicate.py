year = int(input("Input your birth year: "))
# Set the following to user input
month = "November"
day = "20"
name = "Jessica"
sex = "boy"

if (year - 2000) % 12 == 0:
    sign = 'Dragon'
elif (year - 2000) % 12 == 1:
    sign = 'Snake'
elif (year - 2000) % 12 == 2:
    sign = 'Horse'
elif (year - 2000) % 12 == 3:
    sign = 'sheep'
elif (year - 2000) % 12 == 4:
    sign = 'Monkey'
elif (year - 2000) % 12 == 5:
    sign = 'Rooster'
elif (year - 2000) % 12 == 6:
    sign = 'Dog'
elif (year - 2000) % 12 == 7:
    sign = 'Pig'
elif (year - 2000) % 12 == 8:
    sign = 'Rat'
elif (year - 2000) % 12 == 9:
    sign = 'Ox'
elif (year - 2000) % 12 == 10:
    sign = 'Tiger'
else:
    sign = 'Hare'

age = 2019-year
pronouns = "she"
if(sex=="boy"):
    pronouns = "he"
# Change the print method so that it produce the right output.  
print("{} was born on {}/{}/{}. he is currently 99 years old. she was born in the year of the Duck.".format(name, month, day, year, pronouns, age,pronouns, sign))

