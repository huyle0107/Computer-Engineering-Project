import json
import sys
import os
import serial
import time
import threading
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from mqtt import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ReadUart import AnalyzeData

################## Open port ############################

ser = serial.Serial(port = 'COM11', baudrate = 115200)

# Tủ nông nghiệp: 1024 - 600
data = {'NodeID': 0, 'SensorID': 0, 'value': 0}

global giatri
global thread_running
thread_running = True

def toggle_fullscreen(event = None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)
    
    if state:
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    else:
        root.geometry("1024x600")  


################################### bounded the canvas ##################################

def create_rounded_frame(canvas, x0, y0, x1, y1, radius, color):
    canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
    canvas.create_arc(x1 - 2 * radius, y0, x1, y0 + 2 * radius, start=0, extent=90, fill=color, outline=color)
    canvas.create_arc(x0, y1 - 2 * radius, x0 + 2 * radius, y1, start=180, extent=90, fill=color, outline=color)
    canvas.create_arc(x1 - 2 * radius, y1 - 2 * radius, x1, y1, start=270, extent=90, fill=color, outline=color)
    canvas.create_rectangle(x0 + radius, y0, x1 - radius, y1, fill=color, outline=color)
    canvas.create_rectangle(x0, y0 + radius, x1, y1 - radius, fill=color, outline=color)

def resize_rounded_frame(canvas,event):
    canvas.delete("all")  # Clear the canvas
    canvas_width = event.width
    canvas_height = event.height
    create_rounded_frame(canvas, 0, 0, canvas_width, canvas_height, 30, "white")

# Get all values in the Treeview
global values

def get_all_values():
    global values
    values = []
    for item in tree.get_children():
        topic = tree.item(item, "values")[1]
        value = tree.item(item, "values")[2]
        values.append((topic, value))

############################## Set for each frame of canvas ##############################

root = tk.Tk()
# Bind the F11 key to toggle full-screen
root.bind("<F11>", toggle_fullscreen)

# Bind the Escape key to exit full-screen
root.bind("<Escape>", toggle_fullscreen)

# Initial window size (optional)
root.geometry("1024x600")

root.title("Resizable Rounded Frame")
root.config(background="blue")

canvas1 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas1.place(relx=0.01, rely=0.01, relwidth=0.49, relheight=0.48)
canvas2 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas2.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.48)
canvas3 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas3.place(relx=0.01, rely=0.51, relwidth=0.49, relheight=0.48)
canvas4 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas4.place(relx=0.51, rely=0.51, relwidth=0.48, relheight=0.48)

giatri = ""
o1 = "Station Available"
o2 = ""
o3 = "Diary of value"
o4 = "History of "

stringLabel1 = tk.Label(canvas1, text=f'{o1}', bg="white", anchor="w", font=("Arial", 22, "bold"))
stringLabel1.place(relx=0.05, rely=0.05, relwidth=0.8, relheight=0.1)
stringLabel2 = tk.Label(canvas2, text=f'{o2}', bg="white", anchor="w")
stringLabel2.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
stringLabel3 = tk.Label(canvas3, text=f'{o3}', bg="white", anchor="w", font=("Arial", 22, "bold"))
stringLabel3.place(relx=0.05, rely=0.05, relwidth=0.8, relheight=0.1)
stringLabel4 = tk.Label(canvas4, text=f'{o4}', bg="white", anchor="w",  font=("Arial", 25, "bold"))
stringLabel4.place(relx=0.05, rely=0.05, relwidth=0.27, relheight=0.15)

canvas1.bind("<Configure>", lambda event, canvas=canvas1: resize_rounded_frame(canvas, event))
canvas2.bind("<Configure>", lambda event, canvas=canvas2: resize_rounded_frame(canvas, event))
canvas3.bind("<Configure>", lambda event, canvas=canvas3: resize_rounded_frame(canvas, event))
canvas4.bind("<Configure>", lambda event, canvas=canvas4: resize_rounded_frame(canvas, event))



########################### Create for each station ################################

global selected_value2
global thread
thread = None

mqttObject = MQTTHelper()

global WaterLabelTemp
global WaterLabelSal
global WaterLabelPH
global WaterLabelORP
global WaterLabelEC

global SoilLabelTemp
global SoilLabelHumid
global SoilLabelPH
global SoilLabelEC
global SoilLabelN
global SoilLabelP
global SoilLabelK

global AirLabelTemp
global AirLabelHumid
global AirLabelLux
global AirLabelNoise
global AirLabelPM2
global AirLabelPM10
global AirLabelPressure

def create_button():
    
    for widget in canvas2.winfo_children():
        widget.destroy()
    global giatri
    giatri = selected_value.get()
    selected_value2 = tk.StringVar(value="NULL")

    if giatri == "Water Station":

        global WaterLabelTemp
        global WaterLabelSal
        global WaterLabelPH
        global WaterLabelORP
        global WaterLabelEC

        child = ["Temperature", "Salanity", "PH", "ORP", "EC"]

        stringLabel2 = tk.Label(canvas2, text="Water Station", bg="white", anchor="center", font=("Arial", 25, "bold"), fg="blue")
        stringLabel2.place(relx=0.29, rely=0.05, relwidth=0.5, relheight=0.1)

        WaterLabel = tk.Label(canvas2, text="Temperature (℃)", bg="white", anchor="w", font=("Arial", 20), fg="blue")
        WaterLabel.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)

        WaterLabel = tk.Label(canvas2, text="Salanity", bg="white", anchor="w", font=("Arial", 20), fg="blue")
        WaterLabel.place(relx=0.49, rely=0.2, relwidth=0.15, relheight=0.1)

        WaterLabel = tk.Label(canvas2, text="PH", bg="white", anchor="w", font=("Arial", 20), fg="blue")
        WaterLabel.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.1)

        WaterLabel = tk.Label(canvas2, text="ORP (ppm)", bg="white", anchor="w", font=("Arial", 20), fg="blue")
        WaterLabel.place(relx=0.2, rely=0.5, relwidth=0.3, relheight=0.1)

        WaterLabel = tk.Label(canvas2, text="EC (ppm)", bg="white", anchor="w", font=("Arial", 20), fg="blue")
        WaterLabel.place(relx=0.68, rely=0.5, relwidth=0.3, relheight=0.1)

        WaterLabelTemp = tk.Label(canvas2, text="24.89", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="blue")
        WaterLabelTemp.place(relx=0.16, rely=0.29, relwidth=0.5, relheight=0.1)

        WaterLabelSal = tk.Label(canvas2, text="468.79", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="blue")
        WaterLabelSal.place(relx=0.49, rely=0.29, relwidth=0.5, relheight=0.1)

        WaterLabelPH = tk.Label(canvas2, text="6.72", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="blue")
        WaterLabelPH.place(relx=0.785, rely=0.29, relwidth=0.5, relheight=0.1)
        
        WaterLabelORP = tk.Label(canvas2, text="114.0", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="blue")
        WaterLabelORP.place(relx=0.23, rely=0.59, relwidth=0.5, relheight=0.1)

        WaterLabelEC = tk.Label(canvas2, text="0.85", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="blue")
        WaterLabelEC.place(relx=0.705, rely=0.59, relwidth=0.5, relheight=0.1)

        for widget in canvas4.winfo_children():
            widget.destroy()

        labelW = tk.Label(canvas4, text="History of ", bg="white", anchor="w",  font=("Arial", 25, "bold"))
        labelW.place(relx=0.05, rely=0.05, relwidth=0.27, relheight=0.15)

        combobox = ttk.Combobox(canvas4, values=child, font = ("Arial", 23))
        combobox.place(relx=0.28, rely=0.085, relwidth=0.28, relheight=0.075)


    elif giatri == "Soil Station":

        global SoilLabelTemp
        global SoilLabelHumid
        global SoilLabelPH
        global SoilLabelEC
        global SoilLabelN
        global SoilLabelP
        global SoilLabelK

        child = ["Temperature", "Humidity", "PH", "EC", "N", "P", "K"]

        stringLabel2 = tk.Label(canvas2, text="Soil Station", bg="white", anchor="center", font=("Arial", 25, "bold"), fg="red")
        stringLabel2.place(relx=0.29, rely=0.05, relwidth=0.5, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="Temperature (℃)", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="Humidity (%)", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="PH", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.28, rely=0.45, relwidth=0.1, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="EC (ppm)", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.67, rely=0.45, relwidth=0.3, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="N", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.29, rely=0.7, relwidth=0.3, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="P", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.515, rely=0.7, relwidth=0.3, relheight=0.1)

        SoilLabel = tk.Label(canvas2, text="K", bg="white", anchor="w", font=("Arial", 20), fg="red")
        SoilLabel.place(relx=0.74, rely=0.7, relwidth=0.3, relheight=0.1)

        SoilLabelTemp = tk.Label(canvas2, text="24.89", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelTemp.place(relx=0.255, rely=0.29, relwidth=0.5, relheight=0.1)

        SoilLabelHumid = tk.Label(canvas2, text="55.25", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelHumid.place(relx=0.687, rely=0.29, relwidth=0.5, relheight=0.1)

        SoilLabelPH = tk.Label(canvas2, text="6.72", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelPH.place(relx=0.26, rely=0.54, relwidth=0.5, relheight=0.1)
        
        SoilLabelEC = tk.Label(canvas2, text="0.85", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelEC.place(relx=0.7, rely=0.54, relwidth=0.5, relheight=0.1)

        SoilLabelN = tk.Label(canvas2, text="0.85", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelN.place(relx=0.268, rely=0.79, relwidth=0.5, relheight=0.1)

        SoilLabelP = tk.Label(canvas2, text="0.85", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelP.place(relx=0.488, rely=0.79, relwidth=0.5, relheight=0.1)

        SoilLabelK = tk.Label(canvas2, text="0.85", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="red")
        SoilLabelK.place(relx=0.718, rely=0.79, relwidth=0.5, relheight=0.1)

        for widget in canvas4.winfo_children():
            widget.destroy()

        labelS = tk.Label(canvas4, text="History of ", bg="white", anchor="w",  font=("Arial", 25, "bold"))
        labelS.place(relx=0.05, rely=0.05, relwidth=0.27, relheight=0.15)

        combobox = ttk.Combobox(canvas4, values=child, font = ("Arial", 23))
        combobox.place(relx=0.28, rely=0.085, relwidth=0.28, relheight=0.075)


    elif giatri == "Air Station":

        global AirLabelTemp
        global AirLabelHumid
        global AirLabelLux
        global AirLabelNoise
        global AirLabelPM2
        global AirLabelPM10
        global AirLabelPressure

        child = ["Temperature", "Humidity", "Noise", "PM2.5", "PM10", "Atmospheric pressure", "Lux"]

        stringLabel2 = tk.Label(canvas2, text="Air Station", bg="white", anchor="center", font=("Arial", 25, "bold"), fg="green")
        stringLabel2.place(relx=0.29, rely=0.05, relwidth=0.5, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="Temperature (℃)", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.07, rely=0.2, relwidth=0.3, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="Noise", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="Humidity (%)", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.73, rely=0.2, relwidth=0.3, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="PM2.5", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.15, rely=0.45, relwidth=0.3, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="Atmospheric pressure (Kpa)", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.48, rely=0.45, relwidth=0.5, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="PM10", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.157, rely=0.7, relwidth=0.3, relheight=0.1)

        AirLabel = tk.Label(canvas2, text="Lux", bg="white", anchor="w", font=("Arial", 20), fg="green")
        AirLabel.place(relx=0.68, rely=0.7, relwidth=0.3, relheight=0.1)

        AirLabelTemp = tk.Label(canvas2, text="24.89", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelTemp.place(relx=0.15, rely=0.29, relwidth=0.5, relheight=0.1)

        AirLabelNoise = tk.Label(canvas2, text="29.95", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelNoise.place(relx=0.49, rely=0.29, relwidth=0.5, relheight=0.1)

        AirLabelHumid = tk.Label(canvas2, text="67.23", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelHumid.place(relx=0.78, rely=0.29, relwidth=0.5, relheight=0.1)
        
        AirLabelPM2 = tk.Label(canvas2, text="20.51", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelPM2.place(relx=0.15, rely=0.54, relwidth=0.5, relheight=0.1)

        AirLabelPressure = tk.Label(canvas2, text="101.325", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelPressure.place(relx=0.62, rely=0.54, relwidth=0.5, relheight=0.1)

        AirLabelPM10 = tk.Label(canvas2, text="20.51", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelPM10.place(relx=0.15, rely=0.79, relwidth=0.5, relheight=0.1)

        AirLabelLux = tk.Label(canvas2, text="114.0", bg="white", anchor="w", font=("Arial", 25, "bold"), fg="green")
        AirLabelLux.place(relx=0.655, rely=0.79, relwidth=0.5, relheight=0.1)


        for widget in canvas4.winfo_children():
            widget.destroy()

        labelA = tk.Label(canvas4, text="History of ", bg="white", anchor="w",  font=("Arial", 25, "bold"))
        labelA.place(relx=0.05, rely=0.05, relwidth=0.27, relheight=0.15)

        combobox = ttk.Combobox(canvas4, values=child, font = ("Arial", 23))
        combobox.place(relx=0.28, rely=0.085, relwidth=0.28, relheight=0.075)


    elif giatri =="D":
        radiobutton1canvas2 = tk.Radiobutton(canvas2, text="E", variable=selected_value2, value="E", background="white",activebackground="white")
        radiobutton1canvas2.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
        radiobutton2canvas2 = tk.Radiobutton(canvas2, text="F", variable=selected_value2, value="F", background="white", activebackground="white")
        radiobutton2canvas2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
        radiobutton3canvas2 = tk.Radiobutton(canvas2, text="G", variable=selected_value2, value="G", background="white", activebackground="white")
        radiobutton3canvas2.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)


#################### Create a Treeview widget ########################

tree = ttk.Treeview(canvas3,show='headings')
tree["columns"] = ("Name", "Age","cot3")  # Define column names

s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview', rowheight=40)
s.configure("Treeview.Heading", font=("Arial", 15, "bold"))
s.configure("Treeview", font=("Arial", 15, "bold"))

# Create treeview columns
tree.column("#0", width=0, stretch=tk.NO)  # Hidden ID column
tree.column("Name", width=150, minwidth=50, anchor="center")
tree.column("Age", width=150, minwidth=50, anchor="w")
tree.column("cot3", width=150, minwidth=50, anchor="center")

# Define column headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Time", anchor="center")
tree.heading("Age", text="Station and Sensors", anchor="center")
tree.heading("cot3", text="Data of Sensors", anchor="center")
tree.tag_configure('bg', background='#4A6984')
tree.tag_configure('fg', foreground="white")


######################## Update Data #####################

def update_records():
    while (True):
        current_time = time.strftime("%H:%M:%S")

        line = ser.readline().decode('utf-8')
        AnalyzeData(line, data)
        print(data['NodeID'], data['SensorID'], data['value'])

        # time.sleep(3)

        if (data['NodeID'] == "WaterStation"):
            if (data['SensorID'] == "EC"):
                tree.insert("", "0", values=(current_time, "WaterStation/EC", data['value']),tags=('fg', 'bg'))
                WaterLabelEC.config(text = data['value'])
                mqttObject.setPublishData("WaterStation/EC", data['value'])

            if (data['SensorID'] == "SALINITY"):
                tree.insert("", "0", values=(current_time, "WaterStation/SALINITY", data['value']),tags=('fg', 'bg'))
                WaterLabelSal.config(text = data['value'])
                mqttObject.setPublishData("WaterStation/SALINITY", data['value'])

            if (data['SensorID'] == "PH"):
                tree.insert("", "0", values=(current_time, "WaterStation/PH", data['value']),tags=('fg', 'bg'))
                WaterLabelPH.config(text = data['value'])
                mqttObject.setPublishData("WaterStation/PH", data['value'])

            if (data['SensorID'] == "ORP"):
                tree.insert("", "0", values=(current_time, "WaterStation/ORP", data['value']),tags=('fg', 'bg'))
                WaterLabelORP.config(text = data['value'])
                mqttObject.setPublishData("WaterStation/ORP", data['value'])

            if (data['SensorID'] == "TEMP"):
                tree.insert("", "0", values=(current_time, "WaterStation/TEMP", data['value']),tags=('fg', 'bg'))
                WaterLabelTemp.config(text = data['value'])
                mqttObject.setPublishData("WaterStation/TEMP", data['value'])
                
        
        if (data['NodeID'] == "Soil-Station"):
            if (data['SensorID'] == "TEMP"):
                tree.insert("", "0", values=(current_time, "SoilStation/TEMP", data['value']),tags=('fg', 'bg'))
                SoilLabelTemp.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/TEMP", data['value'])

            if (data['SensorID'] == "HUMID"):
                tree.insert("", "0", values=(current_time, "SoilStation/HUMID", data['value']),tags=('fg', 'bg'))
                SoilLabelHumid.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/HUMID", data['value'])

            if (data['SensorID'] == "EC"):
                tree.insert("", "0", values=(current_time, "SoilStation/EC", data['value']),tags=('fg', 'bg'))
                SoilLabelEC.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/EC", data['value'])

            if (data['SensorID'] == "PH"):
                tree.insert("", "0", values=(current_time, "SoilStation/PH", data['value']),tags=('fg', 'bg'))
                SoilLabelPH.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/PH", data['value'])

            if (data['SensorID'] == "N"):
                tree.insert("", "0", values=(current_time, "SoilStation/N", data['value']),tags=('fg', 'bg'))
                SoilLabelN.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/N", data['value'])

            if (data['SensorID'] == "P"):
                tree.insert("", "0", values=(current_time, "SoilStation/P", data['value']),tags=('fg', 'bg'))
                SoilLabelP.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/P", data['value'])

            if (data['SensorID'] == "K"):
                tree.insert("", "0", values=(current_time, "SoilStation/K", data['value']),tags=('fg', 'bg'))
                SoilLabelK.config(text = data['value'])
                mqttObject.setPublishData("SoilStation/K", data['value'])


        if (data['NodeID'] == "Air-Station"):
            if (data['SensorID'] == "TEMP"):
                tree.insert("", "0", values=(current_time, "AirStation/TEMP", data['value']),tags=('fg', 'bg'))
                AirLabelTemp.config(text = data['value'])
                mqttObject.setPublishData("AirStation/TEMP", data['value'])

            if (data['SensorID'] == "HUMID"):
                tree.insert("", "0", values=(current_time, "AirStation/HUMID", data['value']),tags=('fg', 'bg'))
                AirLabelHumid.config(text = data['value'])
                mqttObject.setPublishData("AirStation/HUMID", data['value'])

            if (data['SensorID'] == "LUX"):
                tree.insert("", "0", values=(current_time, "AirStation/LUX", data['value']),tags=('fg', 'bg'))
                AirLabelLux.config(text = data['value'])
                mqttObject.setPublishData("AirStation/LUX", data['value'])

            if (data['SensorID'] == "Noise"):
                tree.insert("", "0", values=(current_time, "AirStation/NOISE", data['value']),tags=('fg', 'bg'))
                AirLabelNoise.config(text = data['value'])
                mqttObject.setPublishData("AirStation/NOISE", data['value'])

            if (data['SensorID'] == "PM2.5"):
                tree.insert("", "0", values=(current_time, "AirStation/PM2", data['value']),tags=('fg', 'bg'))
                AirLabelPM2.config(text = data['value'])
                mqttObject.setPublishData("AirStation/PM2", data['value'])

            if (data['SensorID'] == "PM10"):
                tree.insert("", "0", values=(current_time, "AirStation/PM10", data['value']),tags=('fg', 'bg'))
                AirLabelPM10.config(text = data['value'])
                mqttObject.setPublishData("AirStation/PM10", data['value'])

            if (data['SensorID'] == "Atmospheric pressure"):
                tree.insert("", "0", values=(current_time, "AirStation/PRESSURE", data['value']),tags=('fg', 'bg'))
                AirLabelPressure.config(text = data['value'])
                mqttObject.setPublishData("AirStation/PRESSURE", data['value'])

        
ccc = threading.Thread(target=update_records)
ccc.start()
tree.place(relx=0.1, rely=0.21, relwidth=0.8, relheight=0.77)


#################### Create Radio buttons #####################

selected_value = tk.StringVar(value="A")
def remove_border(event):
    # Remove focus from the Radiobutton to prevent border around the text
    event.widget.master.focus_set()

dataset = ["Water Station", "Soil Station", "Air Station"]

# Set the desired font size for the Radiobutton text
radiobutton_font = ("Arial", 20)

# Set the desired padding for the Radiobutton
padding_width = 40
padding_height = 40

# Create a transparent image as padding
transparent_image = tk.PhotoImage(width=padding_width, height=padding_height)

style = ttk.Style()
style.configure("TRadiobutton", font=radiobutton_font, padding=0, borderwidth=0, background="white")
style.map("TRadiobutton", background=[('active', 'white')])

# Increase the size of the circular part
style.configure("TRadiobutton", indicatorsize=15)

y_offset = 0.01  # Initial value for rely

for i in dataset:
    radiobutton1 = ttk.Radiobutton(
        canvas1, text=i, variable=selected_value, value=i, 
        command=create_button, style="TRadiobutton",
        compound="left", image=transparent_image
    )
    radiobutton1.place(relx=0.05, rely=y_offset + 0.2, relwidth=0.4, relheight=0.1)

    # Bind the event to remove focus and prevent the border
    radiobutton1.bind("<FocusIn>", remove_border)

    y_offset += 0.2


######################## Draw a line chart ########################3
def mqtt_callback(msg):
    print("Main.py  ---", msg)

    data = json.loads(msg)
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
    canvas = FigureCanvasTkAgg(fig, master=canvas4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

mqttObject.setRecvCallBack(mqtt_callback)

root.mainloop()