# Author : Selvasri
# Code : To-DO List using python with the help of tkinter GUI module

# importing GUI modules
import customtkinter
from tkinter import*
from tkinter import messagebox

# creation of frame (or) interface
app=customtkinter.CTk()
app.title("To-DO List")
app.geometry("350x450")
app.config(bg="#09112e")

# denoting the fonts 
font1=("Arial",30,"bold")
font2=("Arial",18,"bold")
font3=("Arial",10,"bold")

# execution of called function
def add_task():
  task=task_entry.get()
  if task:
    tasks_list.insert(0,task)
    task_entry.delete(0,END)
    save_task()
  else:
    messagebox.showerror("ERROR...Please Enter a task...")

def remove_task():
  selected=tasks_list.curselection()
  if selected:
    tasks_list.delete(selected[0])
    save_task()
  else:
    messagebox.showerror("ERROR...Choose a task to delete...")

def save_task():
  with open("task.txt","w") as f:
    tasks = tasks_list.get(0,END)
    for task in tasks:
      f.writer(task + "\n")

def load_task():
  try:
    with open("task.txt","r") as f:
      tasks=f.readlines()
      for task in tasks:
        tasks_list.insert(0,task.strip())
  except FileNotFoundError:
    messagebox.showerror("ERROR","Cannot load tasks...")


# creation of label,button,tasks_list    
title_label=customtkinter.CTkLabel(app,font=font1,text="To-DO List",text_color="#fff",bg_color="#09112e")
title_label.place(x=100,y=20)

add_button=customtkinter.CTkButton(app,command=add_task,font=font2,text="ADD TASK",text_color="#fff",fg_color="#06911f",bg_color="#09112e",hover_color="#06911f",cursor="hand2",corner_radius=5,width=120)
add_button.place(x=40,y=80)

remove_button=customtkinter.CTkButton(app,command=remove_task,font=font2,text="REMOVE TASK",text_color="#fff",fg_color="#96061c",bg_color="#09112e",hover_color="#96061c",cursor="hand2",corner_radius=5)
remove_button.place(x=180,y=80)

task_entry=customtkinter.CTkEntry(app,font=font2,text_color="#000",fg_color="#fff",border_color="#fff",width=280)
task_entry.place(x=40,y=120)

tasks_list=Listbox(app,width=39,height=15,font=font3)
tasks_list.place(x=40,y=180)

load_task()
app.mainloop()
