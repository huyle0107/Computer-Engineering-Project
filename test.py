import serial
import time

# Configure serial port for RS485 communication
ser = serial.Serial(
    port='COM14',  # Change this to your actual serial port
    baudrate=4800,
    timeout=1,
)
# Example: Write data to RS485
data_air_humidity_temperature1 = bytes([0x01, 0x03, 0x07, 0xD0, 0x00, 0x02, 0xC4, 0x86])
data_air_humidity_temperature2 = bytes([0x01, 0x03, 0x01, 0xF4, 0x00, 0x02, 0x84, 0x05])

ser.write(data_air_humidity_temperature1)
print(f"Value1: {data_air_humidity_temperature1}")
print("Data received:", ser.readline())


time.sleep(0.1)  # Allow time for transmission


ser.write(data_air_humidity_temperature2)
print(f"Value2: {data_air_humidity_temperature2}")
print("Data received:", ser.readline())


# Close the serial port
ser.close()












# # Import the required modules
# import tkinter as tk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import paho.mqtt.client as mqtt
# from Subcribe import *
# import time

# # # Create a Tkinter window
# # root = tk.Tk()
# # root.title("Line Chart Example")

# # # Create some sample data for the line chart
# # x = [1, 2, 3, 4, 5]
# # y = [2, 4, 6, 8, 10]

# # # Create a matplotlib figure
# # fig = plt.figure(figsize=(5, 4))
# # ax = fig.add_subplot(111)
# # ax.plot(x, y) # Plot the line chart
# # ax.set_title("A Simple Line Chart")
# # ax.set_xlabel("X-axis")
# # ax.set_ylabel("Y-axis")

# # # Create a canvas widget to display the figure
# # canvas = FigureCanvasTkAgg(fig, master=root)
# # canvas.draw()
# # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # # Start the Tkinter main loop
# # root.mainloop()

# def mqtt_callback(msg):
#     print("Main.py  ---", msg)
#     print("Topic: ", msg.topic)
#     print("Payload: ", msg.payload.decode("utf-8"))

# mqttObject = MQTTHelper()

# while True:
#     mqttObject.setRecvCallBack(mqtt_callback)
#     time.sleep(5)


