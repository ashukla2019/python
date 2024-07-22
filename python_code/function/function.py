Some Benefits of Using Functions:  
1)Increase Code Readability 
2)Increase Code Reusability

Python function declaration sysntax:
def function_name(parameters):
	#statement
	return expression
	
Types of Functions in Python
1) Built-in library function: These are Standard functions in Python that are available to use.
2) User-defined function: We can create our own functions based on our requirements.

# A simple Python function
def fun():
    print("Welcome to GFG")

# Driver code to call a function
fun()

Python Function with Parameters:
If you have experience in C/C++ or Java then you must be thinking about the return type of the function and data type of arguments. 
That is possible in Python as well (specifically for Python 3.5 and above).

def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression
Ex: 
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
evenOdd(2)
evenOdd(3)

Types of Python Function Arguments:
Default argument:A default argument is a parameter that assumes a default value if a value is not provided in the function call for 
that argument
Ex: Python program to demonstrate
# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
# Driver code (We call myFun() with only
# argument)
myFun(10)

Keyword arguments (named arguments): The idea is to allow the caller to specify the argument name with 
values so that the caller does not need to remember the order of parameters.
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)

# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

Positional arguments:We used the Position argument during the function call so that the first argument
(or value) is assigned to name and the second argument (or value) is assigned to age.
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")
 
Arbitrary arguments (variable-length arguments *args and **kwargs):
In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments 
to a function using special symbols. There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)

# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

Anonymous Functions in Python:
In Python, an anonymous function means that a function is without a name. 
As we already know the def keyword is used to define the normal functions and the lambda 
keyword is used to create anonymous functions.
# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

Recursive Functions in Python:
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

What is Python main function?
The Python main function refers to the entry point of a Python program. 
It is often defined using the if __name__ == "__main__": construct to ensure that certain code
is only executed when the script is run directly, not when it is imported as a module.





