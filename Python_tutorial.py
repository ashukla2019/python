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
                                  #Variables:
#We do not need to declare variables before using them or declare their type. A variable is created the moment we first assign a value to it.

# An integer assignment 
age = 45                     
   
# A floating point 
salary = 1456.8            
   
# A string   
name = "John"             
   
print(age) 
print(salary) 
print(name) 

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
						#Taking input from user
#input(): This function first takes the input from the user and then evaluates the expression,
# which means Python automatically identifies whether the user entered 
#a string or a number or list. For example:
# Python program showing a use of input() 
   
val = input("Enter your value: ") 
print(val)

#-----------------------------------------------------------------------------------------------------------------------------------------------
                              #Printing output to console
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
								#Python Data Types
# Numeric(Integer, Float) --> In Python, numeric data type represent the data which has numeric value. Numeric value can be interger, 
# floating number or even complex numbers. These values are defined as int, float and complex.
print("Type of a: ", type(5)) 
print("\nType of b: ", type(5.0)) 
# Dictionary->
# Boolean 
# Set
# Sequence Type ----> Strings, List, Tuples

#--------------------------------------------------------------------------------
#List: mutable, ordered and that's why slicing possible
#Tuple: Immutable, ordered and that's why slicing possible 
#set: mutable, unordered and slicing not possible.

'''
Tuples are more memory efficient than the lists. When it comes to the time efficiency, again tuples have a slight advantage over the lists especially when lookup to a value is considered

'''

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
# For and for-else loop

# for-loop-python
# Python program to illustrate  
# Iterating over a list  
print("List Iteration")  
l = ["geeks", "for", "geeks"]  
for i in l:  
    print(i) 
     
# Iterating over a String  
print("\nString Iteration")      
s = "Geeks"
for i in s :  
    print(i)  
     
print("\nFor-else loop")
for i in s:  
    print(i)  
else: # Executed because no break in for  
    print("No Break\n")  
   
for i in s:  
    print(i)  
    break
else: # Not executed as there is a break  
    print("No Break")  
'''
Output:

List Iteration
geeks
for
geeks

String Iteration
G
e
e
k
s

For-else loop
G
e
e
k
s
No Break

G
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Loop control statements
# Loop control statements change execution from its normal sequence. Following are the loop control statements provided by Python:
# Break: Break statement in Python is used to bring the control out of the loop when some external condition is triggered.
# Continue: Continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.
# Pass: Pass statement is used to write empty loops. Pass is also used for empty control statement, function and classes.

# Python program to demonstrate break, continue and pass 
   
s = 'geeksforgeeks'
 
for letter in s: 
    if letter == 'e' or letter == 's': 
        break
    print(letter)
print()
 
for letter in s: 
    if letter == 'e' or letter == 's': 
        continue
    print(letter)
print()    
 
for letter in s: 
    if letter == 'e' or letter == 's': 
        pass
    print(letter)
'''
Output:

g 
g k f o r g k 
g e e k s f o r g e e k s 
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Functions
# Functions are generally the block of codes or statements in a program that gives the user the ability to reuse the same code which ultimately saves the excessive use of memory, acts as a time saver and more importantly, provides better readability of the code. So basically, a function is a collection of statements that perform some specific task and return the result to the caller. A function can also perform some specific task without returning anything. In Python, def keyword is used to create functions.
# Python program to demonstrate
# functions
 
 
# Defining functions
def ask_user():
    print("Hello Geeks")
 
# Function that returns sum
# of first 10 numbers
def my_func():
    a = 0
    for i in range(1, 11):
        a = a + i
    return a
     
# Calling functions
ask_user()
res = my_func()
print(res)
'''
Output:

Hello Geeks
55
'''


# Function with arguments
# Default arguments: A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
# Python program to demonstrate default arguments 
     
     
def myFun(x, y = 50): 
   print("x: ", x) 
   print("y: ", y) 
       
# Driver code
myFun(10)

'''
Output:

('x: ', 10)
('y: ', 50)
'''

# Keyword arguments: The idea is to allow caller to specify argument name with values so that caller does not need to remember order of parameters.
# Python program to demonstrate Keyword Arguments 
def student(firstname, lastname):  
     print(firstname, lastname)  
     
     
# Keyword arguments                   
student(firstname ='Geeks', lastname ='Practice')     
student(lastname ='Practice', firstname ='Geeks') 

'''
Output:

('Geeks', 'Practice')
('Geeks', 'Practice')
'''

# Variable length arguments: In Python a function can also have variable number of arguments. This can be used in the case when we do not know in advance the number of arguments that will be passed into a function.
# Python program to demonstrate
# variable length arguments
 
 
# variable arguments
def myFun1(*argv):  
    for arg in argv:  
        print(arg) 
         
# variable keyword arguments
def myFun2(**kwargs):
    for key, value in kwargs.items(): 
        print ("% s == % s" %(key, value)) 
   
# Driver code 
myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print()
myFun2(first ='Geeks', mid ='for', last ='Geeks')
'''
Output:

Hello Welcome to GeeksforGeeks 
first == Geeks
last == Geeks
mid == for
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Lambda functions
# In Python, the lambda/anonymous function means that a function is without a name. The lambda keyword is used to create anonymous functions. Lambda function can have any number of arguments but has only one expression.
# Python code to demonstrate   
# labmda function  
 
# Cube using lambda
cube = lambda x: x * x*x  
print(cube(7))
 
# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)
'''
Output:

343
[0, 2, 4, 6, 8]
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

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



