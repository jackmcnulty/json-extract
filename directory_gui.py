#create the main gui for the application

import tkinter as tk
from tkinter import *
import os
import technical_gui

#initialize window
window = tk.Tk()
window.title("JSON Extract")
window.geometry("1280x720") 

#initialize labels and entry boxes
slabel = Label(window, text="Source Folder").pack()
source_folder = tk.Entry(window, width=200, text="Source Folder")
source_folder.pack(side = "top", padx=10, pady = 10)

dlabel = Label(window, text="Destination Folder").pack()
destination_folder = tk.Entry(window, width=200, text="Destination Folder")
destination_folder.pack()

info = Label(
    window, 
    text="Please make sure the filepath includes FORWARD slashes, rather than backslashes", 
    fg="red"
    ).pack()


def storeValue(): #this is the function that gets called when the button is pressed
    global sname, dname
    sname = source_folder.get()
    dname = destination_folder.get()
    
def call_tech():
    technical_gui.gui(sname, dname)
    window.destroy()

#initialize buttons
Button(
    window,
    text= "Select Source and Destination Folder" ,
    padx= 10,
    pady= 5,
    command = lambda: [storeValue(), call_tech()] #call second screen here that actually does stuff
    ).pack()



window.mainloop() # executes tkinter actions