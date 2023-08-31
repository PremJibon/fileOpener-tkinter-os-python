from tkinter import *
from tkinter import filedialog
import os

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system('"%s"' % my_program)

root = Tk()
root.title("Hero Khor")
root.geometry("600x400")

my_button = Button(root,text="Open Program",command=open_program).pack(pady=20)

my_label = Label(root,text='')
my_label.pack(pady=20)

root.mainloop()