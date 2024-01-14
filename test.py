import tkinter as tk
from tkinter import ttk

def on_combobox_click(event):
    combobox.event_generate('<Down>')

root = tk.Tk()

canvas4 = tk.Canvas(root)
canvas4.pack()

child = ["Option 1", "Option 2", "Option 3"]

combobox = ttk.Combobox(canvas4, values=child, font=("Arial", 20))
combobox.place(relx=0.38, rely=0.049, relwidth=0.45, relheight=0.11)

# Increase font size for the dropdown list
combobox.bind('<Button-1>', on_combobox_click)
combobox.option_add('*TCombobox*Listbox.font', ("Arial", 20))

root.mainloop()
