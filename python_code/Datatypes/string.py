#-----------------------------------------------------------------------------------------------------------------------------------------------
# String: A string is a collection of one or more characters put in a single quote, double-quote or triple quote. 
# In python there is no character data type, a character is a string of length one. It is represented by str class. 
# Strings in Python can be created using single quotes or double quotes or even triple quotes.
#      				0  1  2  3  4  5  6  7  8  9  10
#      				A  N  K  I  T  S  H  U  K  L  A
#     				-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 

#-----------------------------------------------Creating a String-------------------------------------------
String1 = "GeeksForGeeks"
     
#-----------------------------------------------Accessing characters in Python----------------------------	 
# Printing First character 
print(String1[0])  
     
# Printing Last character 
print(String1[-1])  

String1 = "Hello, I'm a Geek"
     
#--------------------------------------------------updation and deletion------------------------------------------------------
# Updating a character, will throw an error.
#String1[2] = 'p' //can not modify character by index.
   
# Deleting a character using del will throw an error.  
#del String1[2]

#----------------------------------------------------String Slicing-------------------------------------------------
#To access a range of characters in the String, method of slicing is used. 
#Slicing in a String is done by using a Slicing operator (colon). 
String1 = "GeeksForGeeks"
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:-2])

#Updating Entire String:
String1 = "Hello, I'm a Geek"
String1 = "Welcome to the Geek World"
print(String1)

