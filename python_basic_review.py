# What is python?
# --> it is a genelar purpose programming language known for simplicity and ease of use.
# Common Use Cases:
# --> Pyhton is used in data science, machine learning, web development. cybersecurity, embedded systems and IoT, scripting, automation, and microcomputers such as the raspberry PI and microPython-compatible boards.

# Variables
# Declaring variables:
# --> To declare a variable, you start with the variable name followed by the assignment operator (=) and then the value. This can be a number, string, boolean, etc,
# Here is an example:

name = "Erick Mwangi"
age = 33

# Naming Convention for variables:
# --> Variable names can only start with a letter or an unterscore(_), not a number.
# --> Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores(_).
# --> Variable names are case-sensitive: age, Age and AGE are all considered unique.
# --> Variable names cannot be one of Python's reserved keywords such as if, class, or def.
# --> Variable names wuth multiple words use uderscores, as in snake_case.
# --> Variable names should describle their purpose, as in user_age.
# --> Single-letter variable names should be avoided when they do not communicate meaning

# Comments
# -> Single-Line Comments: This type of comments should be used for short noted in your code.
# -> Multi-line Comments: You can use a # at the beginning of each line to create comments across multiple lines.
# -> print() Function: To print data to the terminal, you use the print() function like this:

print('Hello World!')

# Common Date Types in python
# -> Introduction: Python is dynamically typed language, meaning you don't need to declare a variable's data type. Python determines the type from the value assigned to the variable.
# -> Integer: A whole number without decimals

my_integer_var = 10
print('Interger:', my_integer_var) # Integer: 10

# -> String: A sequence of charaters wrapped in quotes

my_string_var = 'hello'
print('String:', my_string_var) # String: hello

# -> Boolean: A value representing either True or False

my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True

# Python has other data types. You will learn each one when you first need it.
# -> type() Function: To see the type for a variable, you can use the type() function like this:

greeting = 'Hello therer!'
age = 21

print(type(greeting)) # <class 'str'>
print(type(age)) # <class 'int'>

# -> isInstance() Function: This is used to check if a variable matches a specific data type: 

greeting = 'Hello world'
name = 'John Doe'

print(isinstance(greeting, str)) # True
print(isinstance(name, int)) # False

# Working with strings
# -> Definition: Strings are immutable, which means you cannot change them after they have been created. In Python, you can either single or double quotes. Choose one style and use it consistently

developer = "Jessica"
city = 'Los Angeles'

# -> Accessing Charaters from Strings: You can access charaters from strings by using bracket notation like this:

my_str = 'Hello world'

print(my_str[0]) # H
print(my_str[6]) # W

print(my_str[-1]) # d
print(my_str[-2]) # l

# -> Escaping Strings: You can use a backslash(\) if your string contains quotes like this:

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

# -> String Concatenation: To concatenate strings, you can use the + operator like this:

developer = 'Jessica'
print('My name is ' + developer + '.') # My name is Jessica.

# -> f-strings: This is a short for formatted string literals. It allows you to handle interpolation and also do some concatenation with a compact and readable synax:

developer = 'Jessica'
greeting = f'My name is {developer}'
print(greeting) #My name is Jessica

# String Slicing: This is when you extract portions of a string. Here is the basic syntax:
# str[start:stop:step]
# The start postion represent the index where the extration should begin. The stop postion where the slice should end.
# This postion is non inclusive.
# The Step postion represents the interval to increement for the slicing. 
# Here are some examples:

message = 'Python is fun'
print(message[0:6]) # python
print(message[7:]) # is fun!
print(message[::2]) # Pto sfn

# -> Getting the length of a string: The len() function is used to return the number of the characters in the string:

developer = "Jessica"
print(len(developer)) # 7

# Working with the in Operator
# -> in Operator: This returns a boolean that specifies whether the character or characters exist in the string or not:

my_str = 'Hello world'

print('Hello' in my_str) # True
print('hey' in my_str) # False
print('hi' in my_str) # False
print('e' in my_str) # True
print('f' in my_str) # False


# Common String Methods
# -> str.upper(): This returns a new string with all characters converted to uppercase:

developer = 'Jessica'
print(developer.upper()) # JESSICA

# -> str.lower(): This returns a new string with all charaters coverted to lowercase:

developer = 'Jessica'
print(developer.lower()) # jessica

# -> str.strip(): This returns a copy of the string with specified leading and trailing charater removed(if no argument is passed to the method, it removes leading and trailing whitespaces).

greeting = '  hello world  '
trimmed_my_str = greeting.strip()
print(trimmed_my_str) # 'hello world'





