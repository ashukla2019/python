#-------------------------------------------------------------------------------------
#Tuple is a collection of Python objects much like a list. The sequence of values
# stored in a tuple can be of any type, and they are indexed by integers. 
#Values of a tuple are syntactically separated by commas. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. This helps in understanding the Python tuples more easily.
#Creating a Tuple
#In Python, tuples are created by placing a sequence of values separated by comma with or without the use of parentheses for grouping the data sequence.
#Note: Creation of Python tuple without the use of parentheses is known as Tuple Packing. 
 
 #--------------------------------------------------Tuple creation---------------------------------------------------

1. Create
Creating a set involves initializing it with elements, either directly or dynamically.

# Create an empty set
my_set = set()

# Create a set with initial elements
my_set = {1, 2, 3, 4}

# Dynamically populate a set
my_set = set(range(1, 5))
-----------------------------------------------------------------------
2. Read
Reading involves retrieving elements from the set or performing checks on its data.
Check if an element exists:

if 3 in my_set:
    print("3 is in the set")
	
Iterate over the set:
for element in my_set:
    print(element)

Get the size of the set:
size = len(my_set)
--------------------------------------------------------------------------------------------------
3. Update
Updating a set typically involves adding or modifying elements. Sets are unordered and don’t support direct indexing for updates, but new elements can be added, and existing elements can be removed and replaced.
Add elements:
my_set.add(5)  # Add a single element
my_set.update({6, 7, 8})  # Add multiple elements
Replace an element (remove and re-add, since sets don't support direct update):

my_set.remove(2)  # Remove the old element
my_set.add(10)    # Add the new element
------------------------------------------------------------------------------------
4. Delete
Deleting involves removing elements or clearing the set.

Remove a specific element:

my_set.remove(3)  # Raises KeyError if the element doesn't exist
my_set.discard(3)  # Safe, does nothing if the element doesn't exist
Remove and retrieve an arbitrary element:

removed_element = my_set.pop()  # Raises KeyError if the set is empty
Clear the set:


my_set.clear()
Set Operations in CRUD Context
Sets also allow advanced operations like union, intersection, and difference, which are useful in broader CRUD workflows, such as maintaining relationships or subsets.

Union
Combine sets:


set1 = {1, 2, 3}
set2 = {3, 4, 5}
combined = set1.union(set2)  # {1, 2, 3, 4, 5}
Intersection
Find common elements:


common = set1.intersection(set2)  # {3}
Difference
Find elements in one set but not another:


difference = set1.difference(set2)  # {1, 2}
Symmetric Difference
Find elements in either set but not both:


sym_diff = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
These operations can support CRUD functionality in applications like filtering, querying, or comparing data sets.

Example: Set Operations in a CRUD Workflow
Here’s a simple example to demonstrate set operations within a CRUD context:


# Create
users = {"Alice", "Bob", "Charlie"}
new_users = {"Diana", "Eve"}

# Read
if "Bob" in users:
    print("Bob is in the system")

# Update
users.update(new_users)  # Add multiple new users
users.add("Frank")       # Add a single user

# Delete
users.remove("Alice")  # Remove a specific user
users.discard("Zoe")   # Safe removal, no error if "Zoe" doesn't exist

# View all users after operations
print(users)

python tuple operations in CRUD format
Tuples in Python are immutable, meaning their elements cannot be changed after creation. However, you can perform CRUD-like operations by creating new tuples, accessing their elements, or combining tuples. Here's how to approach CRUD operations with tuples:

1. Create
Creating a tuple involves initializing it with elements.

Create an empty tuple:


my_tuple = ()
Create a tuple with elements:

my_tuple = (1, 2, 3, 4)
Create a tuple dynamically:

my_tuple = tuple(range(5))  # (0, 1, 2, 3, 4)
2. Read
Accessing or retrieving elements from a tuple.
Access by index:

print(my_tuple[0])  # First element
Slicing:

print(my_tuple[1:3])  # (2, 3)
Iterate through a tuple:

for element in my_tuple:
    print(element)
Check membership:

if 3 in my_tuple:
    print("3 is in the tuple")
3. Update
Since tuples are immutable, you cannot modify them directly. However, you can create a new tuple based on existing ones.

Simulate an update by creating a new tuple:


my_tuple = (1, 2, 3)
updated_tuple = my_tuple[:1] + (10,) + my_tuple[2:]  # (1, 10, 3)
Append elements by concatenating:


my_tuple = my_tuple + (4,)  # (1, 2, 3, 4)
Replace multiple elements:


my_tuple = (1, 2, 3, 4)
new_tuple = (0,) + my_tuple[1:]  # (0, 2, 3, 4)
4. Delete
Tuples themselves are immutable, so elements cannot be deleted individually. However, you can work around this by creating a new tuple or deleting the entire tuple.

Delete a tuple:


del my_tuple
Remove elements by reconstructing:


my_tuple = (1, 2, 3, 4)
filtered_tuple = tuple(x for x in my_tuple if x != 3)  # (1, 2, 4)
Tuple Operations in CRUD Context
Tuples can also be used in conjunction with tuple-specific operations to perform CRUD-like behaviors:

Combine (Concatenation)
Combine tuples to simulate adding new elements:


tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)
Repeat
Repeat a tuple multiple times:


repeated = tuple1 * 3  # (1, 2, 1, 2, 1, 2)
Count or Index
Retrieve information about elements:

my_tuple = (1, 2, 3, 2)
count = my_tuple.count(2)  # 2 occurrences of 2
index = my_tuple.index(3)  # Index of first occurrence of 3
Example: Tuple Operations in CRUD Workflow
Here's an example demonstrating CRUD principles with tuples:


# Create
inventory = ("apple", "banana", "cherry")

# Read
if "banana" in inventory:
    print("Banana is available")

# Update (simulate by creating a new tuple)
inventory = inventory + ("orange",)  # Add new item
inventory = tuple(item for item in inventory if item != "cherry")  # Remove "cherry"

# Delete (delete the entire tuple)
del inventory

# Output after each operation
print(inventory)  # Results based on the operations performed
