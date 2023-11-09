# Import the required modules
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("Line Chart Example")

# Create some sample data for the line chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a matplotlib figure
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111)
ax.plot(x, y) # Plot the line chart
ax.set_title("A Simple Line Chart")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Create a canvas widget to display the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the Tkinter main loop
root.mainloop()
