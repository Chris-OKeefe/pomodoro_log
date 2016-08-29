from Tkinter import *
from ttk import *

def task_logger(args*):
  #task = raw_entry()
  #put text into pomodoro_log.txt: date, time, task

def timer(args*):
  #break = take data from break widget (float)
  #work = take data from pom widget (float)
  #set alarm for t minutes after break, work

root = Tk()
root.title("Pomodoro Task Logger")

mainframe = Frame(root, padding = "1 6 N N")
mainframe.grid(column=0, row=0, sticky = (N,W,E,S) #initialize grid?
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

task = StringVar()
date
time
break_length = float()
work_length = float()

task_entry = Entry(mainframe, width = 20, textvariable = task)
task_entry.grid(column = 1, row = 2, sticky = W)

break_entry = Entry(mainframe, width = 5, numeric? = break_length)
break_entry.grid(column = 1, row = 4, sticky = W)

work_entry = Entry(mainframe, width = 5, numeric? = work_length)
work_entry.grid(column = 1, row = 6, sticky = W)

Button(mainframe, text = "Enter", command = task_logger)

Label(mainframe, text = "Current Task").grid(column = 1, row = 1, sticky = W)
Label(mainframe, text = "Break Length").grid(colunn = 1, row = 3, sticky = W)
Label(mainframe, text = "Work Time").grid(column = 1, row = 5, sticky = W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5) #$

task_entry.focus()
root.bind('<Return>', task_logger, timer) # I want <return> to do both functions

root.mainloop()
