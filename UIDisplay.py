import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

window = tk.Tk()
combo_var = tk.StringVar()

def center_window(width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window position
    window.geometry(f'{width}x{height}+{x}+{y}')


def on_select(event):
    selected_option = combo_var.get()
    result_label.config(text = f"Selected Option: {selected_option}")

def WidgetOption():
    options = ["Option 1", "Option 2", "Option 3"]
    combo = ttk.Combobox(window, textvariable = combo_var, values = options)
    combo.pack(padx = 10, pady = 10)
    combo.bind("<<ComboboxSelected>>", on_select)


def frame(color):
    frame = tk.Frame(window, width = 100, height = 100, bg = color)
    # frame1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
    frame.pack(padx = 1, pady = 1)




if __name__ == "__main__":

    window.title("")
    # Set size and make in center of screen
    center_window(800, 500)

    frame1 = frame("white")
    label = tk.Label(frame1, text = "Choose an option:")
    label.pack()

    #define the second frame
    WidgetOption()

    # define the second frame
    frame2 = frame("gray")
    result_label = tk.Label(frame2, text = "Selected Option: ")
    result_label.pack(padx = 10, pady = 10)



    
    window.mainloop()