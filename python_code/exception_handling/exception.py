'''
Exception Handling in Python
Exception Handling is used to handle situations in our program flow, which can
inevitably crash our program and hamper its normal working. It is done in Python
using try-except-finally keywords.
try: The code in try section is the part of the code where the code is to be tested
for exceptions.
except: Here, the cases in the original code, which can break the code, are
written, and what to do in that scenario by the program.
finally: The code in the finally block will execute whether or not an exception
has been encountered by the program.
'''

# divide(4, 2) will return 2 and print Division Complete
# divide(4, 0) will print error and Division Complete
# Finally block will be executed in all cases
def divide(a, denominator):
	try:
		return a / denominator
	except ZeroDivisionError as e:
		print('Divide By Zero!! Terminate!!')
	finally:
		print('Division Complete.')
