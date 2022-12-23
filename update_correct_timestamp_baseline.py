import Tkinter as tk
import os, stat
import re
from time import strftime
import Tkinter, Tkconstants, tkFileDialog
import random
from Tkinter import *
Path = ""


root = tk.Tk()
root.geometry("400x300")
l1 = tk.Label(root, text="Baseline_Name", bg='cyan', bd=5)
l1.pack()
entry1 = tk.Entry(root, bd=5)
entry1.place(height = 40, width=250, x=80, y=40)


def browse_path():
	global Path
	Path = tkFileDialog.askdirectory()
	Path = Path.replace("/", "\\")

browse_path = tk.Button(root, text="Browse Source Path", command=browse_path, bd=6, bg="yellow")
browse_path.place(width=200, x=100, y=100)



def changeBaseLine(filename, Baseline):
	with open(filename, 'r+') as f:
		text = f.read()
		text = re.sub("Baseline.*", Baseline,text)
		f.seek(0)
		f.write(text)
		f.truncate()
	
def changeTimeStamp(filename):
	with open(filename, 'r+') as f:
			text = f.read()
			str = strftime("%d/%m/%Y %I:%M:%S %p")
			s = list(str)
			text = re.sub(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}.*", str, text)
			f.seek(0)
			f.write(text)
			f.truncate()
	
	
def Perform_operation():
	Baseline = entry1.get()
	Baseline = 'Baseline: ' +  Baseline
	for root, dirs, files in os.walk(Path):
		for file in files:
			if file.endswith(".tst"):
				filename = os.path.join(root, file)
				os.chmod(filename, stat.S_IWRITE)
				changeTimeStamp(filename)
				changeBaseLine(filename,Baseline)
				
	print "End"
	
	
update_button = tk.Button(root, text="Update BaseLine & TimeStamp", command=Perform_operation, bd=6, bg='green')
update_button.place(width=200, x=100, y=150)

root.mainloop()