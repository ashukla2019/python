#-----------------------------------------------------------------------------------------------------------------------------------------------
#Lists in Python can be created by just placing the sequence inside 
#the square brackets[].
#Unlike Sets, list does not need a built-in function for creation of list.
#Note  Unlike Sets, list may contain mutable elements.
  
#---------------------------------------------- Creating/Initilizing a List---------------------------------------------------------
List = []
print("Blank List: ")
print(List)
  
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
  
# Creating a List of strings and accessing using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0]) 
print(List[2])
  
# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Geeks', 'For'] , ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)
'''
Output:
Blank List: 
[]

List of numbers: 
[10, 20, 14]

List Items
Geeks
Geeks

Multi-Dimensional List: 
[['Geeks', 'For'], ['Geeks']]
'''

#Creating a list with multiple distinct or duplicate elements
#A list may contain duplicate values with their distinct positions and hence, 
#multiple distinct or duplicate values can be passed as a sequence at the time 
#of list creation.

# Creating a List with 
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
  
# Creating a List with mixed type of values
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

'''
Output:
List with the use of Numbers: 
[1, 2, 4, 4, 3, 3, 3, 6, 5]

List with the use of Mixed Values: 
[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
'''

#Knowing the size of List
# Creating a List
List1 = []
print(len(List1))
  
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

#-----------------------------------------Adding Elements---------------------------------------------------
#Using append() method:Elements can be added to the List by using built-in append() function.
#Only one element at a time can be added to the list by using append() method,
#for addition of multiple elements with the append() method, loops are used. 
#Tuples can also be added to the List with the use of append method because tuples
#are immutable. Unlike Sets, Lists can also be added to the existing list with 
#the use of append() method.

# Creating a List
List = []
print("Initial blank List: ")
print(List)
  
# Addition of Elements 
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
  
# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
  
# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)
  
# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

'''
Output:
Initial blank List: 
[]

List after Addition of Three elements: 
[1, 2, 4]

List after Addition of elements from 1-3: 
[1, 2, 4, 1, 2, 3]

List after Addition of a Tuple: 
[1, 2, 4, 1, 2, 3, (5, 6)]

List after Addition of a List: 
[1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]
'''

#Using insert() method
#append() method only works for addition of elements at the end of the List,
#for addition of element at the desired position, insert() method is used. 
#Unlike append() which takes only one argument, insert() method requires two 
#arguments(position, value).

# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
  
# Addition of Element at 
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
'''
Output:
Initial List: 
[1, 2, 3, 4]

List after performing Insert Operation: 
['Geeks', 1, 2, 3, 12, 4]

'''
#Using extend() method
#Other than append() and insert() methods, there is one more method for Addition 
#of elements, extend(), this method is used to add multiple elements at the same 
#time at the end of the list.
#Note  append() and extend() methods can only add elements at the end.
    
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
  
# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)
'''
Output:
Initial List: 
[1, 2, 3, 4]

List after performing Extend Operation: 
[1, 2, 3, 4, 8, 'Geeks', 'Always']
'''
#--------------------------------------------Accessing:Slicing of a List--------------------------------------------------
#In Python List, there are multiple ways to print the whole List with all the elements,
#but to print a specific range of elements from the list, we use Slice operation.
#Slice operation is performed on Lists with the use of a colon(:). 
#To print elements from beginning to a range use [: Index], to print elements 
#from end-use [:-Index], to print elements from specific Index till the end use [Index:], to print elements within a range, use [Start Index:End Index] and to print the whole List with the use of slicing operation, use [:]. Further, to print the whole List in reverse order, use [::-1].
#Note  To print elements of List from rear end, use Negative Indexes.

# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Initial List: ")
print(List)
  
# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)
  
# Print elements from a 
# pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)
  
# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)
'''
Output:
Initial List: 
['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

Slicing elements in a range 3-8: 
['K', 'S', 'F', 'O', 'R']

Elements sliced from 5th element till the end: 
['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

Printing all elements using slice operation: 
['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
'''
#Negative index List slicing
# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Initial List: ")
print(List)
  
# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)
  
# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)
  
# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
'''
Output:

Initial List: 
['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

Elements sliced till 6th element from last: 
['G', 'E', 'E', 'K', 'S', 'F', 'O']

Elements sliced from index -6 to -1
['R', 'G', 'E', 'E', 'K']

Printing List in reverse: 
['S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G']
'''

#------------------------------------------------Removing Elements from the List-----------------------------------
#Using remove() method
#Elements can be removed from the List by using built-in remove() function but an Error
#arises if element does not exist in the set. Remove() method only removes one element at a time, 
#to remove range of elements, iterator is used. The remove() method removes the specified item.

#Note  Remove method in List will only remove the first occurrence of the searched element.
  
# Creating a List
List = [1, 2, 3, 4, 5, 6, 
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
  
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)
  
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)

'''
Output:
Initial List: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

List after Removal of two elements: 
[1, 2, 3, 4, 7, 8, 9, 10, 11, 12]

List after Removing a range of elements: 
[7, 8, 9, 10, 11, 12]

'''

#Using pop() method
#Pop() function can also be used to remove and return an element from the set, 
#but by default it removes only the last element of the set, to remove element 
#from a specific position of the List, index of the element is passed as an argument
#to the pop() method.

List = [1,2,3,4,5]
  
# Removing element from the 
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)
  
# Removing element at a 
# specific location from the 
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
'''
Output:
List after popping an element: 
[1, 2, 3, 4]

List after popping a specific element: 
[1, 2, 4]
'''

