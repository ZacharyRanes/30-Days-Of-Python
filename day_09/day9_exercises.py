"""
Get user input using input(“Enter your age: ”).
If user is 18 or older, give feedback: You are old enough to drive.
If below 18 give feedback to wait for the missing amount of years.
"""

age = input("Enter your age: ")
if int(age) < 18:
    print("You need {} more years to learn to drive.".format(18-int(age)))
else:
    print("You are old enough to learn to drive.")


