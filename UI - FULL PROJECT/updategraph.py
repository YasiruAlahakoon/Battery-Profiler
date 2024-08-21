import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

new_value_exists = True
# Function to update the plot with new data
def update_plot():
    x = np.linspace(0, update_plot.counter, update_plot.counter + 1)
    y = np.sin(x)
    # Clear the previous plot
    ax.clear()
    # Plot the new data
    ax.plot(x, y)
    # Update the plot
    canvas.draw()
    # Increment counter for dynamic data
    update_plot.counter += 1
    # Schedule the next update if new data exists
    global new_value_exists
    if new_value_exists:
        root.after(100, update_plot)
        #new_value_exists = False
    
# Counter for dynamic data (replace this with your data retrieval logic)
update_plot.counter = 0

# Create Tkinter application window
root = tk.Tk()
root.title("Dynamic Plot")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Pack the Matplotlib canvas widget into the Tkinter window
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a button to fill the remaining space
button = tk.Button(root, text="This is a Button")
button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Initial plot
update_plot()

# Start the Tkinter event loop
root.mainloop()