#-----------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary
# Dictionary in Python is an unordered collection of data values, used to store data values like a
# map. Dictionary holds key:value pair. Each key-value pair in a Dictionary is separated by a
# colon :, whereas each key is separated by a comma. A Dictionary can be created by placing a 
# sequence of elements within curly {} braces, separated by comma.
# Creating an empty Dictionary  
Dict = {}
print(Dict)  
 
# with Integer Keys  
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)  
 
# with Mixed keys  
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict) 
'''
Output:

{}
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
{1: [1, 2, 3, 4], 'Name': 'Geeks'}
'''

#Nested-Dictionary
# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For',  
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
   
print(Dict)  
'''
Output:

{1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
'''

# Adding elements to a Dictionary: One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = Value.
# Creating an empty Dictionary 
Dict = {}
   
# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict) 
 
   
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print(Dict) 
'''
Output:

{0: 'Geeks', 2: 'For', 3: 1}
{0: 'Geeks', 2: 'Welcome', 3: 1}
'''

# Accessing elements from a Dictionary: In order to access the items of a dictionary refer to its key name or use get() method.
# Python program to demonstrate accessing an element from a Dictionary   
     
# Creating a Dictionary   
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}  
     
# accessing a element using key
print(Dict['name'])  
   
# accessing a element using get()
print(Dict.get(3)) 
'''
Output:

For
Geeks
'''
# Removing Elements from Dictionary: Using pop() and popitem()
# Initial Dictionary  
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',  
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
       }  
     
# using pop()  
Dict.pop(5) 
print(Dict)  
 
# using popitem()  
Dict.popitem() 
print(Dict)  

'''
Output:

{'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'}, 6: 'To', 7: 'Geeks'}
{6: 'To', 7: 'Geeks'}
'''
