import os
import shutil

mydir = r"C:\Users\z00427jp\Desktop\RBC\Automate\Test"

#function to find files ending with extension .txt or .cpp in directory
def find_file_in_dir():
    for root, dirs, files in os.walk(mydir): #unpacking root,directory and files from os.walk(mydir)
        #root = directory path, dirs = directory inside path, files = files inside path
        for file in files:
            if file.endswith(".txt") or file.endswith(".cpp"):
                print(os.path.join(root, file))
                path_out = os.path.join(root, file)
                path_current = r"D:\docs\new"
                shutil.copy2(path_out, path_current)
                #shutil.rmtree(path_current)
                
find_file_in_dir()