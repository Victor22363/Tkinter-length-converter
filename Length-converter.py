import tkinter as tk
import ttkbootstrap as ttk
#from tkinter import ttk

# !!!pack is like a reverse stack!!!

# functions
def convert():
    i = int(entryVar.get())
    checked_value = listVar.get()
    statment1 = list[1]
    statment2 = list[2]
    if checked_value == statment1:
        i *= 1.6093445
    elif checked_value == statment2:
        i *= 0.621371192
    output_text.set(i)

# window
window = ttk.Window(themename="darkly")
window.title("Length converter")
window.geometry("500x200")

# title
title_label = ttk.Label(master=	window, text="Converter", font="Calibri 24")
title_label.pack()

# dropdown menu
list = ["Pls select" , "Km --> Mi", "Mi --> Km"]
listVar = ttk.StringVar()
listVar.set(list[0])
menu = ttk.OptionMenu(window, listVar ,*list)
menu.pack()

# input field
input_frame = ttk.Frame(master= window)
entryVar = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable= entryVar)
button = ttk.Button(master= input_frame, text="Convert", command= convert)
window.bind("<Return>", lambda event=None: button.invoke()) # if i press enter key it makes everything in that lambda func. execute!
entry.pack(side="left", padx= 10)
button.pack(side="right")
input_frame.pack(pady= 10)

#output field
output_text = tk.StringVar()
output_frame = ttk.Frame(master= window)
output = ttk.Label(master= output_frame, textvariable=output_text, font= "Calibry 14")
output.pack(side="left")
output_frame.pack()

# run
window.mainloop()