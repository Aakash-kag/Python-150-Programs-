#Write a Python program to Chech Leap Year.
year = int(input("Enter a year: "))

if (year % 400 == 0 and year % 100 == 0):
    print("{0} is a leap year".format(year))
elif(year % 4 == 0 and year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not leap year".format(year))