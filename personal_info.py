#Taking user input
name = input("What is your name?: ")
age = input("How old are you?: ")
birthday = input("When is your birthday?: ")
address = input("What is your address?: ")

#Printing result
print("Hello " + age + " year old " + name + " of "+ address + ". I have made a note to remember your birthday on " + birthday)
print("Hello {} year old {} of {}. I have made a note to remember your birthday on {}.".format(age, name, address, birthday))
print(f"Hello {age} year old {name} of {address}. I have made a note to remember your birthday on {birthday}.")

#Note: All three methods will print the exact same result
