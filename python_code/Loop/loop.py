'''
Loop Statements in Python
Loops in Python are statements that allow us to perform a certain operation multiple
times unless some condition is met.
For Loops: For loop is used to iterate iterables like string, tuple, list, etc and perform
some operation as shown in the flowchart below:
'''

#For with range:
#This loop format will iterate overall numbers from 0 to Limit - 1.
#The below example prints numbers from 0 to 4.
for i in range(5):
	print(i)

'''
Output:
0
1
2
3
4
'''

#For with range(start, stop, step):
#This will run the loop from start to stop - 1, with step size = step in each iteration.
#In the below example, the start is 2, end point is 10 and the step size is 2. Hence it

for i in range(2, 10, 2):
	print(i)
'''
Output:
2
4
6
8
'''

#For with in:
#This is used to iterate over all the elements in a python container like list,
#tuple, dictionary, etc.

a = [1, 3, 5, 7]
for ele in a:
	print(ele)
	
'''	
Output:
1
3
5
7
'''


#While Loops:
#This is used for executing set of statements within its block as long as the
#associated loop condition is evaluated to True as shown in the image below:

count = 5
while count > 0:
	print(count)
	count -= 1

output:
'''
5
4
3
2
1
'''
