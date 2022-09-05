#!/usr/bin/python3

from ttkwidgets import CheckboxTreeview
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree = CheckboxTreeview(root)
tree.pack()

tree.insert("", "end", "1", text="1")
tree.insert("1", "end", "11", text="11")
tree.insert("1", "end", "12",  text="12")
tree.insert("11", "end", "111", text="111")
tree.insert("", "end", "2", text="2")

tree.expand_all()

def check_function():
    tree.check_all()

def uncheck_function():
    tree.uncheck_all()

check_button = ttk.Button(root, text='check all', command=check_function)
check_button.pack()

uncheck_button = ttk.Button(root, text='uncheck all', command=uncheck_function)
uncheck_button.pack()

root.mainloop()
