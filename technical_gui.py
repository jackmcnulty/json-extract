import tkinter as tk
from tkinter import *
import os


def gui(sname, dname):
    window = tk.Tk()
    window.title("JSON Extract")
    window.geometry("1280x720")

    frame = Frame(window)
    #frame.pack(side="left", fill="both", expand=True)
    frame.grid(row=1, column=0, rowspan=5, columnspan=2, padx=2, pady=2)
    directory = Listbox(frame)
    directory.grid(row=1, column=0, rowspan=5, columnspan=2, padx=2, pady=2)
    for file in os.listdir(sname):
        directory.insert(END, file)

