# Import the tkinter module
import tkinter
import os, stat
import re
from tkinter import filedialog
import random
import shutil, glob, re, datetime
from datetime import date
from tkinter import *

#Global Variables for path and file type
Path = ""
file_extension = ""

#Create UI Screen
root = tkinter.Tk()
root.geometry("500x500")
root.title("Smart_Reporter")

# Create the list of options
file_extension_list = [".txt", ".slf", ".cpp", ".c"]

# Variable to keep track of the option selected in OptionMenu
file_extension_list_value = tkinter.StringVar(root)

# Set the default value of the variable
file_extension_list_value.set("Select file extension type")

# declaring string variable
text_var=tkinter.StringVar()

def browse_path():
    #print(file_extension_list_value.get())
    #browse_path.configure(relief = "flat")
    global Path
    Path = filedialog.askdirectory()
    Path = Path.replace("/", "\\")    
    
 
def check_expiry():
    ext = file_extension_list_value.get()
    root1 = tkinter.Tk()
    root1.geometry("500x500")
    root1.title("Check_Expiry")

    # Add a Scrollbar(horizontal)
    v=Scrollbar(root1, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    # Add a text widget
    text=Text(root1, font=("Georgia, 10"), yscrollcommand=v.set)
    word = '<end_date>'
    for root, dirs, files in os.walk(Path): 
        for file in files:
            if file.endswith(ext):
                
                path_out = os.path.join(root, file)
                with open(path_out, 'r') as fp:
                    # read all lines in a list
                    lines = fp.readlines()
                    for line in lines:
                        # check if string present on a current line
                        if line.find(word) != -1:
                            day = re.search('\d{4}-\d{2}-\d{2}', line)
                            date1 = datetime.datetime.strptime(day.group(), '%Y-%m-%d').date()
               
                            if(date.today()> date1):
                                #lExpired.write('\n'+path_out)
                                text.insert(END, path_out+'\n')
                    
                            else:
                                pass
                                #lNotExpired.write('\n'+path_out)
                            break;
                        
                        else:
                            pass
    print("all files checked")
    v.config(command=text.yview)
    text.pack()
    root1.mainloop()
    
def search_text():
    ext = file_extension_list_value.get()
    root2 = tkinter.Tk()
    root2.geometry("500x500")
    root2.title("Check_Expiry")
     # Add a Scrollbar(horizontal)
    v=Scrollbar(root2, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    # Add a text widget
    text=Text(root2, font=("Georgia, 10"), yscrollcommand=v.set)
    for root, dirs, files in os.walk(Path): 
        for file in files:
            #print(file)
            if file.endswith(ext):
                path_out = os.path.join(root, file)
                with open(path_out, 'r') as fp:
                    # read all lines in a list
                    lines = fp.readlines()
                    if entry1.get():
                        word = entry1.get()
                        for line in lines:
                            #check if string present on a current line
                            if re.search(r'\b' + word + r'\b', line):
                                text.insert(END, path_out+ line+'\n')
                    else:
                        print("please enter text to search")
    v.config(command=text.yview)
    text.pack()
    root2.mainloop()                   
        

file_extension_menu = tkinter.OptionMenu(root, file_extension_list_value, *file_extension_list)
file_extension_menu.pack()

browse_path = tkinter.Button(root, text="Browse Source Path", command=browse_path, bd=6, bg="yellow")
browse_path.place(width=250, x=100, y=60)

l1 = tkinter.Label(root, text="Enter Text to search", bg='cyan', bd=5).place(x = 100, y = 120)
entry1 = tkinter.Entry(root, bd=5)
entry1.place(height = 40, width=250, x=100, y=150)
	
search_button = tkinter.Button(root, text="Search_Text", command=search_text, bd=6, bg='green')
search_button.place(width=125, x=350, y=150)
    
search_button = tkinter.Button(root, text="Check_Expiry", command=check_expiry, bd=6, bg='green')
search_button.place(width=250, x=100, y=250)


# Attach the scrollbar with the text widget


root.mainloop()