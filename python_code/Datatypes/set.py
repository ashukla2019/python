
# Set
# In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. 
#The order of elements in a set is undefined though it may consist of various elements. Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces {}, separated by comma.
# Python program to demonstrate Creation of Set in Python  
     
#------------------------------------------------------------- Creating a Set--------------------------------------------- 
set1 = set()  
 
# Creating a Set of String  
set1 = set("GeeksForGeeks") 
print(set1)  
   
# Creating a Set of List  
set1 = set(["Geeks", "For", "Geeks"])
print(set1)  
'''
Output:

{'o', 'r', 'k', 'G', 'e', 's', 'F'}
{'Geeks', 'For'}
'''
#---------------------------------------------------------------- Adding elements: Using add() and update()--------------------
# Python program to demonstrate Addition of elements in a Set  
  
set1 = set()
     
# Adding to the Set using add() 
set1.add(8)
set1.add((6, 7))
print(set1)  
   
# Additio to the Set using Update()   
set1.update([10, 11])
print(set1) 
'''
Output:

{8, (6, 7)}
{8, 10, 11, (6, 7)}
'''
#----------------------------------- Accessing a Set: One can loop through the set items using a for loop as set items cannot be accessed #by referring to an index.
# Python program to demonstrate Accessing of elements in a set  
     
# Creating a set  
set1 = set(["Geeks", "For", "Geeks"])  
 
# Accessing using for loop
for i in set1:  
    print(i)
'''
Output:

Geeks For
''' 

#---------------------------------------------------------- Removing elements from a set: Using remove(), discard(), pop() and clear()
# Python program to demonstrate Deletion of elements in a Set  
 
set1 = set([1, 2, 3, 4, 5, 6,   
            7, 8, 9, 10, 11, 12])  
 
# using Remove() method  
set1.remove(5)  
set1.remove(6)
print(set1)  
 
# using Discard() method  
set1.discard(8)  
set1.discard(9)
print(set1)  
 
# Set using the pop() method  
set1.pop()
print(set1)  
 
# Set using clear() method  
set1.clear()
print(set1) 
'''
Output:

{1, 2, 3, 4, 7, 8, 9, 10, 11, 12}
{1, 2, 3, 4, 7, 10, 11, 12}
{2, 3, 4, 7, 10, 11, 12}
set()
'''

