"""
Python is a high-level programming language and is widely being used among the developers community.
Python was mainly developed for emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code.
"""
#Python Indentation:
#Python uses indentation to highlight the blocks of code. Whitespace is used for indentation in Python.

#Python Comments:
	#Single line comments: Python single line comment starts with hash tag symbol with no white spaces.
	# This is a comment 
	#Multi-line string as comment: Python multi-line comment is a piece of text enclosed in a delimiter (''') on each end of the comment.
""" 
This would be a multiline comment in Python that...
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------
                              #Printing output to console
# print(hello) => NameError: name 'hello' is not defined
# One object is passed 
print("GeeksForGeeks") 
   
x = 5
# Two objects are passed 
print("x =", x) 
   
# code for disabling the soft space feature  
#print('G', 'F', 'G', sep ='') 
   
# using end argument 
#print("Python", end = '@')   
#print("GeeksforGeeks")  Python@GeeksforGeeks
#-----------------------------------------------------------------------------------------------------------------------------------------------
                                  #Variables:
#We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it.
-> No special character is allowed
-> starting with number not allowed

# An integer assignment 
age = 45                     
   
# A floating point 
salary = 1456.8            
   
# A string   
name = "John"
name1 = 'ABC'

#Bool
True
False
   
print(age) 
print(salary) 
print(name) 
print(name1)

#-----------------------------------------------------------------------------------------------------------------------------------------------
						#Taking input from user
#input(): Whatever value is entered, it is taken as string so it should be converted to specific data types.
   
val = input("Enter your value: ")
Enter your value: 10
print(type(val)) => o/p: <class 'str'>

#-----------------------------------------------------------------------------------------------------------------------------------------------
                                 # Operators:
#Arithmetic operators: Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.
	# Examples of Arithmetic Operator 
	a = 9
	b = 4
   
	# Addition of numbers 
	add = a + b 
	# Subtraction of numbers  
	sub = a - b 
   
	# print results 
	print(add) 
	print(sub) 

#Relational Operators: Relational operators compares the values. It either returns True or False according to the condition:
	# Examples of Relational Operators 
	a = 13
	b = 33
	   
	# a > b is False 
	print(a > b) 
	   
	# a < b is True 
	print(a < b) 
	   
	# a == b is False 
	print(a == b) 
   
	# a != b is True 
	print(a != b) 
	   
	# a >= b is False 
	print(a >= b) 
	   
	# a <= b is True 
	print(a <= b)

#Logical Operators: Logical operators perform Logical AND, Logical OR and Logical NOT operations.
	# Examples of Logical Operator 
	a = True
	b = False
	   
	# Print a and b is False 
	print(a and b) 
	   
	# Print a or b is True 
	print(a or b) 
	   
	# Print not a is False 
	print(not a) 

#Bitwise operators: Bitwise operator acts on bits and performs bit by bit operation.
	# Examples of Bitwise operators 
	a = 10
	b = 4
	   
	# Print bitwise AND operation   
	print(a & b) 
	   
	# Print bitwise OR operation 
	print(a | b) 
	   
	# Print bitwise NOT operation  
	print(~a) 
	   
	# print bitwise XOR operation  
	print(a ^ b) 
	   
	# print bitwise right shift operation  
	print(a >> 2) 
	   
	# print bitwise left shift operation  
	print(a << 2)

#Assignment operators: Assignment operators are used to assign values to the variables.
	#Special operators: Special operators are of two types-
	
	#Identity operator that contains is and is not.
	#Membership operator that contains in and not in.
	
	# Examples of Identity and 
	# Membership operator
	  
	a1 = 'GeeksforGeeks'
	b1 = 'GeeksforGeeks'
	 
	# Identity operator
	print(a1 is not b1)
	print(a1 is b1)
	 
	# Membership operator
	print("G" in a1)
	print("N" not in b1)

#-----------------------------------------------------------------------------------------------------------------------------------------------
Strings:
hello= 'hello'
print(type(hello)) => <class 'str'>

Creating Strings
	# Single quotes
	string1 = 'Hello, world!'
	
	# Double quotes
	string2 = "Python is fun!"
	
	# Triple quotes for multiline strings
	string3 = """This is a
	multiline string."""

Basic String Operations
	# Concatenation
	combined = string1 + " " + string2
	
	# Repetition
	repeated = string1 * 3
	
	# Length
	length = len(string1)
	
	# Accessing characters
	first_char = string1[0]
	last_char = string1[-1]
	
	# Slicing
	substring = string1[0:5]
	String Methods
	
	# Changing case
	upper_case = string1.upper()
	lower_case = string1.lower()
	
	# Splitting and joining
	words = string2.split()  # Splits into a list of words
	joined = " ".join(words)  # Joins list into a string
	
	# Stripping whitespace
	trimmed = "  Hello  ".strip()
	
	# Replace
	replaced = string1.replace("world", "Python")
	
	# Finding substrings
	index = string1.find("world")  # Returns -1 if not found
	
	# Checking content
	is_alpha = "abc".isalpha()
	is_digit = "123".isdigit()
	String Formatting
	
	# f-strings (Python 3.6+)
	name = "Alice"
	formatted = f"Hello, {name}!"
	
	# format() method
	formatted = "Hello, {}!".format(name)
	
	# Old-style formatting
	formatted = "Hello, %s!" % name
	Escape Characters
	
	# Newline and tab
	new_line = "Hello\nWorld"
	tabbed = "Hello\tWorld"
	
	# Escape quotes
	quote = "She said, \"Python is awesome!\""

Strings are immutable in Python, so methods that modify a string return a new string.
Use r"raw strings" to avoid escaping backslashes in paths or regex patterns.
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Decision Making
# Decision Making in programming is similar to decision making in real life. A programming language uses control statements to control the flow of execution of the program based on certain conditions. These are used to cause the flow of execution to advance and branch based on changes to the state of a program.

# Decision-making statements in Python
#    if statement
#    if..else statements
#    nested if statements
#    if-elif ladder

#Example 1: To demonstrate if and if-else
# Python program to demonstrate
# decision making
 
a = 10
b = 15
 
# if to check even number
if a % 2 == 0:
    print("Even Number")
     
# if-else to check even or odd
if b % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
'''
Output:

Even Number
Odd Number
'''
# Example 2: To demonstrate nested-if and if-elif
# Python program to demonstrate
# decision making
 
a = 10
 
# Nested if to check whether a 
# number is divisible by both 2 and 5
if a % 2 == 0:
    if a % 5 == 0:
        print("Number is divisible by both 2 and 5")
         
# is-elif
if (a == 11): 
    print ("a is 11") 
elif (a == 10): 
    print ("a is 10")
else: 
    print ("a is not present")
'''
Output:

Number is divisible by both 2 and 5
a is 10
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Control flow (Loops)
# Loops in programming come into use when we need to repeatedly execute a block of statements. For example: Suppose we want to print 'Hello World' 10 times. 
# This can be done with the help of loops. The loops in Python are:

# Python program to illustrate  
# while and while-else loop
i = 0
while (i < 3):      
    i = i + 1
    print("Hello Geek")  
   
# checks if list still 
# contains any element  
a = [1, 2, 3, 4] 
while a: 
    print(a.pop()) 
   
i = 10
while i < 12:  
    i += 1
    print(i)  
    break
else: # Not executed as there is a break  
    print("No Break") 
'''
Output:

Hello Geek
Hello Geek
Hello Geek
4
3
2
1
11
'''
---------------------------------------------------------------------------------------------------------------------------------------------	
# For and for-else loop
A for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any object that supports iteration. 
Here's the basic syntax:
for variable in sequence:
    # Code block to execute
	
1. Iterating Over a List:
	fruits = ["apple", "banana", "cherry"]
		for fruit in fruits:
	    	print(fruit)
	Output:
	apple
	banana
	cherry
2. Iterating Over a String:
	word = "Python"
	for letter in word:
	    print(letter)
	Output:
	P
	y
	t
	h
	o
	n
3. Using range(): The range() function generates a sequence of numbers.
	for i in range(5):
	    print(i)
	Output:	
	0
	1
	2
	3
	4
	Example with start and end:
	for i in range(1, 6):
	    print(i)
	Output:		
	1
	2
	3
	4
	5

	Example with step:
	for i in range(0, 10, 2):
	    print(i)
	Output:
	0
	2
	4
	6
	8
4. Iterating Over a Dictionary:
	person = {"name": "Alice", "age": 25, "city": "New York"}
	for key, value in person.items():
	    print(f"{key}: {value}")
	Output:
	name: Alice
	age: 25
	city: New York
5. Nested For Loops:
	for i in range(3):
	    for j in range(2):
	        print(f"i={i}, j={j}")
	Output:
	i=0, j=0
	i=0, j=1
	i=1, j=0
	i=1, j=1
	i=2, j=0
	i=2, j=1
6. break and continue in For Loops:
	break: Exits the loop entirely.
	continue: Skips the current iteration and moves to the next.
	Example with break:
	for i in range(5):
	    if i == 3:
	        break
	    print(i)
	Output:
	0
	1
	2
	Example with continue:
	python
	Copy code
	for i in range(5):
	    if i == 3:
	        continue
	    print(i)
	Output:
	0
	1
	2
	4
7. else with For Loops:
	An else block after a for loop executes only if the loop completes normally (i.e., not terminated by a break).
	for i in range(5):
	    print(i)
	else:
	    print("Loop finished without a break.")
	Output:
	0
	1
	2
	3
	4
	Loop finished without a break.
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Functions
# Functions are generally the block of codes or statements in a program that gives the user the ability to reuse the same code which ultimately saves the excessive use of memory, acts as a time saver and more importantly, provides better readability of the code. So basically, a function is a collection of statements that perform some specific task and return the result to the caller. A function can also perform some specific task without returning anything. In Python, def keyword is used to create functions.
# Python program to demonstrate
# functions
 
1. Direct Function Call
The most common way to call a function.
	def greet():
    		print("Hello!")

	greet()  # Output: Hello!

2. Function Call with Arguments: Functions can accept arguments and return values.
	def add(a, b):
    		return a + b

	result = add(5, 3)  # result = 8
	print(result)

3. Using Default Arguments: If arguments are not provided, the default values are used.
	def greet(name="Guest"):
    		print(f"Hello, {name}!")
	greet()           # Output: Hello, Guest!
	greet("Alice")    # Output: Hello, Alice!

4. Using Keyword Arguments: You can specify arguments by name, in any order.
	def introduce(name, age):
    		print(f"My name is {name} and I'm {age} years old.")
	introduce(age=25, name="Bob")  # Output: My name is Bob and I'm 25 years old.

5. Passing Arbitrary Arguments: For unknown or variable numbers of arguments, use *args or **kwargs.
	def display(*args, **kwargs):
    		print("Positional arguments:", args)
    		print("Keyword arguments:", kwargs)

	display(1, 2, 3, name="Alice", age=25)
	# Output:
	# Positional arguments: (1, 2, 3)
	# Keyword arguments: {'name': 'Alice', 'age': 25}
											     
6. Calling Functions Dynamically: Using a reference to the function.
	def greet():
    		print("Hello!")

	func = greet  # Assign function to a variable
	func()        # Output: Hello!
	    
7. Calling Functions from a Dictionary: Functions can be stored in dictionaries and called dynamically.
	def add(a, b):
    		return a + b

	def subtract(a, b):
   	 return a - b

	operations = {
	    "add": add,
	    "subtract": subtract
	}

	result = operations["add"](10, 5)  # result = 15
	print(result)

8. Calling a Method on an Object: When using classes, methods are called using the dot operator.
	class Greeter:
    		def greet(self):
       			print("Hello from a class!")

	greeter = Greeter()
	greeter.greet()  # Output: Hello from a class!

9. Using eval() or exec(): Avoid these for security reasons unless absolutely necessary.
	code = "print('Hello from eval')"
	eval(code)  # Output: Hello from eval

10. Calling Anonymous Functions (lambda): Lambdas are small, inline functions.
	add = lambda x, y: x + y
	print(add(3, 5))  # Output: 8

11. Using functools.partial: Partial functions pre-fill some arguments.
	from functools import partial

	def power(base, exponent):
    		return base ** exponent

	square = partial(power, exponent=2)
	print(square(4))  # Output: 16

12. Using map, filter, and reduce: Higher-order functions to apply a function to iterables.
	nums = [1, 2, 3, 4]
	squared = list(map(lambda x: x**2, nums))
	print(squared)  # Output: [1, 4, 9, 16]

13. Using a Function Pointer in Modules:You can reference and call functions dynamically by their name in a module.
	import math
	func_name = "sqrt"
	result = getattr(math, func_name)(16)  # Call math.sqrt(16)
	print(result)  # Output: 4.0
#-----------------------------------------------------------------------------------------------------------------------------------------------
Data Types:

---------------------------------------------------------------------------------------------------------------------------------------------------------
# Object Oriented Programming
# Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc in programming. 
# The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function

# Classes and Objects
# Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.
# An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values.
# Python program to demonstrate classes and objects
   
class Dog:  
       
    # A simple class attribute
    attr1 = "mamal"
    attr2 = "dog"
   
    # A sample method   
    def fun(self):  
        print("I'm a", self.attr1) 
        print("I'm a", self.attr2) 
   
# Driver code 
# Object instantiation 
Rodger = Dog() 
   
# Accessing class attributes 
# and method through objects 
print(Rodger.attr1) 
Rodger.fun()
'''
Output:

mamal
I'm a mamal
I'm a dog
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------

# The self
# self represents the instance of the class. By using the self keyword 
# we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
# Note: For more information, refer self in Python class.
# Constructors and Destructor

# Constructors: Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of 
# the class when an object of class is created. In Python the __init__() method is called the constructor and is always called when an object is created. There can be two types of constructors:
# Default constructor: The constructor which is called implicilty and do not accept any argument.
# Parameterized constructor:Constructor which is called explicitly with parameters is known as parameterized constructor.

# Python program to demonstrate constructors
 
 
class Addition:
    # parameterized constructor 
    def __init__(self, f, s): 
        self.first = f 
        self.second = s
   
    def calculate(self):
        print(self.first + self.second)
   
# Invoking parameterized constructor
obj = Addition(1000, 2000) 
   
# perform Addition 
obj.calculate() 

'''
Output:

3000
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------
# Destructors: Destructors are called when an object gets destroyed. The __del__() method is a known as a destructor method in Python. It is called when all references to the object have been deleted i.e when an object is garbage collected.
# Python program to illustrate destructor 
class Employee: 
   
    # Initializing 
    def __init__(self): 
        print('Employee created.') 
   
    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called, Employee deleted.') 
   
obj = Employee() 
del obj 

'''
Output:

Employee created.
Destructor called, Employee deleted.
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Inheritance
# Inheritance is the ability of any class to extract and use features of other classes. It is the process by which new classes called the derived classes are created from existing classes called Base classes.
# A Python program to demonstrate inheritance  
   
 
class Person(): 
       
    # Constructor 
    def __init__(self, name): 
        self.name = name 
   
    # To get name 
    def getName(self): 
        return self.name 
   
    # To check if this person is employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
# Driver code 
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
   
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee())

'''
Output:

Geek1 False
Geek2 True
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Encapsulation
# Encapsulation describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
# Python program to demonstrate encapsulation 
   
# Creating a Base class 
class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
   
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
           
        # Calling constructor of 
        # Base class
        Base.__init__(self)  
        print("Calling private member of base class: ") 
        print(self.__a) 
# Driver code 
#obj = Derived()

'''
Output:

Traceback (most recent call last):
  File "/home/5a605c59b5b88751d2b93dd5f932dbd5.py", line 20, in 
    obj = Derived()
  File "/home/5a605c59b5b88751d2b93dd5f932dbd5.py", line 18, in __init__
    print(self.__a) 
AttributeError: 'Derived' object has no attribute '_Derived__a'
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Polymorphism
# Polymorphism refers to the ability of OOPs programming languages to differentiate between entities with the same name efficiently. This is done by Python with the help of the signature of these entities.
# Python program to demonstrate Polymorphism
 
 
class A():
    def show(self):
        print("Inside A")
         
class B():
    def show(self):
        print("Inside B")
         
# Driver's code
a = A()
a.show()
b = B()
b.show()

'''
Output:

Inside A
Inside B
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------
# File Handling



