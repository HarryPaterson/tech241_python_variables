#Importing Datetime
from datetime import datetime
#Taking user input
name = input("What is your name?: ")
address = input("What is your address?: ")
dob = input("Enter your date of birth (YYYY-MM-DD):")
#Calculating age
now = datetime.now()
birthday = datetime.strptime(dob, "%Y-%m-%d")
difference = now - birthday
age = difference.days // 365

#Printing result
print(f"Hello {age} year old {name} of {address}. I have made a note to remember your birthday on {birthday.day}/{birthday.month}.")