python- list is ordered and mutable. It is ordered, so we can perform slicing on it.
Python lists can be used to implement CRUD (Create, Read, Update, Delete) operations effectively.
Here's a breakdown of how each operation works in the context of lists:

1. Create: Adding Elements to a List
Creating or adding elements to a list can be done using methods like append(), extend(), or insert().

# Create an empty list
my_list = []

# Add elements
my_list.append(10)           # Adds 10 to the end of the list
my_list.append(20)           # Adds 20 to the end of the list
print(my_list)               # Output: [10, 20]

# Add multiple elements
my_list.extend([30, 40])     # Adds elements from another iterable
print(my_list)               # Output: [10, 20, 30, 40]

# Add element at a specific index
my_list.insert(2, 25)        # Inserts 25 at index 2
print(my_list)               # Output: [10, 20, 25, 30, 40]
----------------------------------------------------------------------------------------------
2. Read: Accessing Elements in a List
Reading elements can be done using indexing, slicing, or iteration.

# List for demonstration
my_list = [10, 20, 30, 40, 50]

# Access element by index
print(my_list[0])            # Output: 10 (first element)
print(my_list[-1])           # Output: 50 (last element)

# Access a slice of the list
print(my_list[1:4])          # Output: [20, 30, 40]

# Iterate through the list
for item in my_list:
    print(item)
# Output:
# 10
# 20
# 30
# 40
# 50
----------------------------------------------------------------------------------------
3. Update: Modifying Elements in a List
Updating elements involves changing specific elements by their index or updating multiple elements using slicing.

# List for demonstration
my_list = [10, 20, 30, 40, 50]

# Update a single element
my_list[2] = 35             # Update index 2 with 35
print(my_list)              # Output: [10, 20, 35, 40, 50]

# Update multiple elements using slicing
my_list[1:3] = [25, 45]     # Replace elements at index 1 and 2
print(my_list)              # Output: [10, 25, 45, 40, 50]

# Append or insert elements to add new data
my_list.append(60)          # Add 60 to the end
my_list.insert(1, 15)       # Insert 15 at index 1
print(my_list)              # Output: [10, 15, 25, 45, 40, 50, 60]
-------------------------------------------------------------------------------------
4. Delete: Removing Elements from a List
Deleting elements can be done using del, remove(), pop(), or slicing.

# List for demonstration
my_list = [10, 20, 30, 40, 50]

# Remove by index using del
del my_list[2]             # Removes the element at index 2
print(my_list)             # Output: [10, 20, 40, 50]

# Remove by value using remove()
my_list.remove(20)         # Removes the first occurrence of 20
print(my_list)             # Output: [10, 40, 50]

# Remove the last element using pop()
last_element = my_list.pop()  # Pops and returns the last element
print(last_element)           # Output: 50
print(my_list)                # Output: [10, 40]

# Remove multiple elements using slicing
my_list = [10, 20, 30, 40, 50]
my_list[1:4] = []           # Removes elements at index 1 to 3
print(my_list)              # Output: [10, 50]

# Clear the entire list
my_list.clear()             # Empties the list
print(my_list)              # Output: []

--------------------------------------------------------------------------------------------------
Full CRUD Workflow Example

# Initialize an empty list (Create)
students = []

# Add students to the list (Create)
students.append("Alice")
students.append("Bob")
students.append("Charlie")
print("Students after adding:", students)  # Output: ['Alice', 'Bob', 'Charlie']

# Read the list of students
print("Student at index 1:", students[1])  # Output: Bob
print("All students:", students)          # Output: ['Alice', 'Bob', 'Charlie']

# Update a student's name
students[1] = "Bobby"
print("Students after update:", students) # Output: ['Alice', 'Bobby', 'Charlie']

# Delete a student by name
students.remove("Alice")
print("Students after deletion:", students) # Output: ['Bobby', 'Charlie']

# Clear all students
students.clear()
print("Students after clearing:", students) # Output: []
