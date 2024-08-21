from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label, Entry, Text
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from tkinter import Toplevel
import struct
import spidev

# # State machine for SPI:
# # Send a current value
# # 0: Ask if value is available
# # STM32 replies with 0 if value is not available, n, qith number of values if has
# # 1 Ask for values
# # 2 Stop discharging
# # STM32 replies with required data. May be multiple bytes
# # For connection check: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

spi = spidev.SpiDev()
spi.open(0, 0)  # Open bus 0, device (CS) 0

# Set SPI parameters
spi.max_speed_hz = 500000  # Set speed to 500 kHz (adjust as needed)
spi.mode = 0b00  # SPI mode (depends on your STM32 setup)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1024x600")
window.configure(bg = "#000000")
window.attributes("-fullscreen", True)
common_canvas = Canvas(window, bg = "#000000", height = 600, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
common_canvas.create_rectangle(0.0, 0.0, 1024.0, 59.0, fill = "#B27A27", outline = "")
common_canvas.create_rectangle(965.0, 0.0, 1024.0, 600.0, fill = "#B27A27", outline = "")
common_canvas.create_text(66.0, -12.0, anchor = "nw", text = "BatteryBeam", fill = "#FFFFFF", font = ("Homenaje Regular", 40))
common_canvas.create_text(525.0, 10.0, anchor = "nw", text = "Battery Profiler & Emulator", fill = "#FFFFFF", font = ("Gruppo", 30))
image_image_1 = PhotoImage(file = relative_to_assets("logo.png"))
image_1 = common_canvas.create_image(36.0, 29.0, image = image_image_1)
common_canvas.place(x = 0, y = 0)

def set_screen():
    
    # button_1.destroy()
    # button_2.destroy()
    # button_3.destroy()
    start_button.destroy()
    label_1.destroy()
    
    def insert_number(number):
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + str(number))

    def clear_entry():
        entry.delete(0, tk.END)

    def on_enter(entry):
    # Function to be called when Enter is pressed
        data = entry.get()
        if data == "":
            entry.delete(0, tk.END)
            return
        if int(data) == 0:
            entry.delete(0, tk.END)
            return
        if int(data) > 30:
            data = 30
        spi.xfer([int(data)])
        entry.destroy()
        number0.destroy()
        number1.destroy()
        number2.destroy()
        number3.destroy()
        number4.destroy()
        number5.destroy()
        number6.destroy()
        number7.destroy()
        number8.destroy()
        number9.destroy()
        clear.destroy()
        enter.destroy()
        l.destroy()
        constant_voltage(current_level=int(data))
    l = Label(window, text="Enter the current level", font=('Arial', 30), bg="#000000", fg="#ffffff")
    l.place(x=300, y=100)
    entry = Entry(window, font=('Arial', 20))
    entry.place(x = 340, y = 250)
    entry.bind("<Return>", lambda event: on_enter(entry))
    buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            'Clear', '0', 'Enter'
    ]
    number_1_image = PhotoImage(file=relative_to_assets("1 (Custom).png"))
    number1 = Button(image=number_1_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(1), relief="flat")
    number1.image = number_1_image
    number1.place(x = 350, y = 350)
    number_2_image = PhotoImage(file=relative_to_assets("2 (Custom).png"))
    number2 = Button(image=number_2_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(2), relief="flat")
    number2.image = number_2_image
    number2.place(x = 450, y = 350)
    number_3_image = PhotoImage(file=relative_to_assets("3 (Custom).png"))
    number3 = Button(image=number_3_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(3), relief="flat")
    number3.image = number_3_image
    number3.place(x = 550, y = 350)
    number_4_image = PhotoImage(file=relative_to_assets("4 (Custom).png"))
    number4 = Button(image=number_4_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(4), relief="flat")
    number4.image = number_4_image
    number4.place(x = 350, y = 400)
    number_5_image = PhotoImage(file=relative_to_assets("5 (Custom).png"))
    number5 = Button(image=number_5_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(5), relief="flat")
    number5.image = number_5_image
    number5.place(x = 450, y = 400)
    number_6_image = PhotoImage(file=relative_to_assets("6 (Custom).png"))
    number6 = Button(image=number_6_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(6), relief="flat")
    number6.image = number_6_image
    number6.place(x = 550, y = 400)
    number_7_image = PhotoImage(file=relative_to_assets("7 (Custom).png"))
    number7 = Button(image=number_7_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(7), relief="flat")
    number7.image = number_7_image
    number7.place(x = 350, y = 450)
    number_8_image = PhotoImage(file=relative_to_assets("8 (Custom).png"))
    number8 = Button(image=number_8_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(8), relief="flat")
    number8.image = number_8_image
    number8.place(x = 450, y = 450)
    number_9_image = PhotoImage(file=relative_to_assets("9 (Custom).png"))
    number9 = Button(image=number_9_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(9), relief="flat")
    number9.image = number_9_image
    number9.place(x = 550, y = 450)
    number_0_image = PhotoImage(file=relative_to_assets("0 (Custom).png"))
    number0 = Button(image=number_0_image, borderwidth=0, highlightthickness=0, command=lambda: insert_number(0), relief="flat")
    number0.image = number_0_image
    number0.place(x = 450, y = 500)
    clear_image = PhotoImage(file=relative_to_assets("clear (Custom).png"))
    clear = Button(image=clear_image, borderwidth=0, highlightthickness=0, command=clear_entry, relief="flat")
    clear.image = clear_image
    clear.place(x = 350, y = 500)
    enter_image = PhotoImage(file=relative_to_assets("enter (Custom).png"))
    enter = Button(image=enter_image, borderwidth=0, highlightthickness=0, command=lambda: on_enter(entry), relief="flat")
    enter.image = enter_image
    enter.place(x = 550, y = 500)
 

def get_reading():
    # This function should return the new reading value
    reading_array = []
    data_to_receive = spi.xfer([0])
    for i in range(int(data_to_receive[0])):
        received_data = spi.xfer([0x00, 0x00, 0x00 & 0x0F])
        combined_value = (received_data[0] << 12) | (received_data[1] << 4) | (received_data[2] & 0x0F)

# Convert to decimal integer
        decimal_value = int(combined_value) * 5 / 1048575 # 5V reference, 20-bit ADC
        reading_array.append(decimal_value)
    avg_reading = np.mean(reading_array)
    # Step 2: Convert the received bytes to a floating point number
    return avg_reading

def back():
    global backpressed
    Canvas
    backpressed = True
    spi.xfer([0x02])

def constant_voltage(current_level:int):
    global backpressed, samples, readings, backbutton, canvas, label_3, label_4
    backpressed = False
    samples = []
    readings = []
    
    # button_1.destroy()
    # button_2.destroy()
    # button_3.destroy()
    start_button.destroy()
    label_1.destroy()


    backbutton_image = PhotoImage(file=relative_to_assets("back.png")) # Change this to back button image
    backbutton = Button(
        image=backbutton_image,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    backbutton.image = backbutton_image
    backbutton.place(x=22, y=520, width=200*0.9, height=80*0.9)

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.set_xlabel("Time")
    plot.set_ylabel("Voltage")
    plot.set_title("Voltage vs Time")
    plot.grid()
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=50, width=750, height=400)
    label_3 = Label(main_frame, text="Current level", bg="#000000", fg="#ffffff", font=("Gruppo", 18))
    label_3.place(x=810, y=40)
    label_4 = Label(main_frame, text=f"{current_level} A", bg="#000000", fg="#ffffff", font=("Gruppo", 25))
    label_4.place(x=810, y=90)
    def update_plot():
        if backpressed:
            reset_main_screen()
            return
        plot.clear()
        samples.append(len(readings))
        readings.append(get_reading())
        plot.plot(samples, readings)
        plot.set_xlabel("Time")
        plot.set_ylabel("Voltage")
        plot.set_title("Voltage vs Time")
        plot.set_xlim(0, ((len(samples) // 100) + 1) * 100)
        plot.set_ylim(0, 7)   # Adjust as necessary based on expected reading values
        plot.grid()
        canvas.draw()
        window.after(1000, update_plot)

    update_plot()

def reset_main_screen():
    backbutton.destroy()
    label_3.destroy()
    label_4.destroy()
    global label_1, button_1, button_2, button_3, canvas, start_button
    canvas.get_tk_widget().destroy()
    label_1 = Label(main_frame, text="Welcome", bg="#000000", fg="#ffffff", font=("Gruppo", 45))
    label_1.place(x=380, y=10)
    
    # button_image_1 = PhotoImage(file=relative_to_assets("constantvoltage.png"))
    # button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=set_screen, relief="flat")
    # button_1.image = button_image_1
    # button_1.place(x=76.0, y=200.0, width=250, height=110)

    # button_image_2 = PhotoImage(file=relative_to_assets("constantcurrent.png"))
    # button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=set_screen, relief="flat")
    # button_2.image = button_image_2
    # button_2.place(x=644.0, y=200.0, width=250, height=110)

    # button_image_3 = PhotoImage(file=relative_to_assets("constantpower.png"))
    # button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=set_screen, relief="flat")
    # button_3.image = button_image_3
    # button_3.place(x=360.0, y=385.0, width=250, height=110)

    start_button_image = PhotoImage(file=relative_to_assets("start.png"))
    start_button = Button(image=start_button_image, borderwidth=0, highlightthickness=0, command=set_screen, relief="flat")
    start_button.image = start_button_image
    start_button.place(x=380, y=300.0, width=250, height=110)

    window.bind('<Escape>', close_window)


def close_window(event):
    window.destroy()

main_frame = Frame(window, bg="#000000", height=541, width=965, bd=0, highlightthickness=0, relief="ridge")
label_1 = Label(main_frame, text="Welcome", bg="#000000", fg="#ffffff", font=("Gruppo", 45))
label_1.place(x=380, y=10)
window.bind('<Escape>', close_window)
# button_image_1 = PhotoImage(file=relative_to_assets("constantvoltage.png"))
# button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=set_screen, relief="flat")
# button_1.image = button_image_1
# button_1.place(x=76.0, y=200.0, width=250, height=110)

# button_image_2 = PhotoImage(file=relative_to_assets("constantcurrent.png"))
# button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
# button_2.image = button_image_2
# button_2.place(x=644.0, y=200.0, width=250, height=110)

# button_image_3 = PhotoImage(file=relative_to_assets("constantpower.png"))
# button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
# button_3.image = button_image_3
# button_3.place(x=360, y=385.0, width=250, height=110)

start_button_image = PhotoImage(file=relative_to_assets("start.png"))
start_button = Button(image=start_button_image, borderwidth=0, highlightthickness=0, command=set_screen, relief="flat")
start_button.image = start_button_image
start_button.place(x=380, y=300.0, width=250, height=110)

main_frame.place(x=0, y=59)

window.mainloop()