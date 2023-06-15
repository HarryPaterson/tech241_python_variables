<h1 style="text-align: center;">Intro to Python</h1>

### Contents
* Variables
* Data Types
* Booleans

### Variables

Variables are used to store data in memory and give them a name for easy reference. In Python, you can create a variable by assigning a value to it using the assignment operator (=). For example:

```
x = 1
y = 2.5
name = "Harry"
```
Python is dynamically typed, meaning you don't need to explicitly declare the type of a variable. The type is inferred based on the value assigned to it.
Variables can store different types of data such as integers, floats and strings as seen above.

Variables can be used in expressions and operations. You can perform arithmetic operations, concatenate strings, and more using variables. To get the value stored in a variable, you can simply refer to the variable by its name. For example:
   ```
   x = 1
y = 2.5
z = x + y
print(z)
   ```
Result : 3.5
### Data Types

The simple data types we have just seen are integers (whole numbers without decimal points), floats (numbers with decimal points) and strings (sequences of characters enclosed in single ' ' or double " " quotes). We can use some inbuilt functions to manage operations using multiple data types. In this example we'll be using int() and str():
```
x = 16
y = '1'

print(x + y)
print('The number of trainees is' + x)
```
Both of these print statements will result in **errors.**  Addition is unsupported for integers and strings and only strings can be concatenated. The correct print statements would be:
```
print(x + int(y))
print('The number of trainees is ' + str(x))
```
##### Exercise

With the input() function we can request a user to input various data. Using this and your knowledge of data types and print statements create a simple application to gather a users name, age, date of birth and address and display it back to them.
<details>
  <summary>Solution</summary>

```
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
```


</details>

<details>
  <summary>Bonus solution!</summary>

##### Adding Datetime

Our personal info app is sufficient but to make our user's life even easier we can use Datetime. Datetime will allow us to work out the users age using their D.O.B. and lower the number of required user inputs from an overbearing 4 to a manageable 3!
```
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
```

Note: The product owner is asking what's taking so long, the user has entered their info wrong and is experiencing an error. Sometimes, less is more.
</details>

### Booleans

Booleans are a data type in Python that represents two truth values: **True** and **False**. They are keywords and should always be capitalized.
Boolean values are the result of comparison operators and logical operations. Comparison operators include equal to (==), not equal to (!=), greater than (>), less than (<), etc.
Booleans can be converted to other data types. When converted to integers, True becomes 1 and False becomes 0.
They can be stored in variables and used in expressions just like other data types. For example:
```
x = True
y = False
z = x and y  # z will be False

print (x==y) # returns false
print (x== False) # returns false
print (y>= False) # returns true
print (x==True) # returns true
```
In Python, other than true or false there is also **None**. This is a special value in Python that represents the absence of a value or the lack of a return value from a function. It serves as a placeholder or indicator for empty or uninitialized variables, objects, or function results.
None is considered a falsy value in Python. This means that when None is evaluated in a conditional statement, it is treated as false.
Avoid using == to compare with None since it may yield unexpected results. The recommended approach is to use the 'is' operator to check for None explicitly.
```
x = None
if x is None:
    print("x is None")  # Output: x is None

```

# tech241_python_variables
