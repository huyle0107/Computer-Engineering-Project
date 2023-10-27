import sys
import os
import serial
import tkinter as tk

from ReadUart import AnalyzeData

ser = serial.Serial(port = 'COM4', baudrate = 115200)

title_watermonitoring = ["Temperature", "Salinity", "EC", "ORP"]
title_soilmonitoring = ["Temperature", "Humidity", "PH", "EC", "N", "P", "K"]
title_airmonitoring = ["Temperature", "Humidity", "Lux", "CO2"]
title = [title_watermonitoring, title_soilmonitoring, title_airmonitoring]

# Tủ nông nghiệp: 1024 - 600
data = {'NodeID': 0, 'SensorID': 0, 'value': 0}
n = 5

class UpdateLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.update_text()

    def update_text(self):
        line = ser.readline().decode('utf-8')
        print(line)
        AnalyzeData(line, data)
        print(data['NodeID'], data['SensorID'], data['value'])

        self.config(text = f"{data['NodeID']}, {data['SensorID']}, {data['value']}")
        self.after(1000, self.update_text)


root = tk.Tk()
root.attributes('-fullscreen', True)  # Set the window to fullscreen
root.configure(bg='#000C66')

# Create three frames, each occupying a column
frame1 = tk.LabelFrame(root, bg='lightblue')
frame2 = tk.Frame(root, bg='lightgreen')
frame3 = tk.Frame(root, bg='lightyellow')

# Configure grid to create three equal columns
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Place frames in grid
frame1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
frame3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

# Create labels for each frame
label1 = UpdateLabel(frame1, text='Label 1', fg='black', bg='lightblue', font=('Arial', 16))
label2 = tk.Label(frame2, text='Label 2', fg='black', bg='lightgreen', font=('Arial', 16))
label3 = tk.Label(frame3, text='Label 3', fg='black', bg='lightyellow', font=('Arial', 16))

# Pack the labels inside the frames
label1.pack(expand=True)
label2.pack(expand=True)
label3.pack(expand=True)

root.mainloop()














"""from ListNodeBox import *
from ListSensorBox import *
from TopThirdGroupBox import *
from TableData import *
from ReadUart import AnalyzeData

from PyQt5.QtGui import QCursor, QPixmap, QIcon, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QThread
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog, QMainWindow, QDesktopWidget)
class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        # self.originalPalette = QApplication.palette()

        # styleComboBox = QComboBox()
        # styleComboBox.addItems(QStyleFactory.keys())

        # styleLabel = QLabel("&Style:")
        # styleLabel.setBuddy(styleComboBox)

        # self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        # self.useStylePaletteCheckBox.setChecked(True)

        # disableWidgetsCheckBox = QCheckBox("&Disable widgets")
        self.worker = WorkerThread()
        self.worker.start()
        createTopFirstGroupBox(self, data)
        createTopSecondGroupBox(self, n)
        createTopThirdGroupBox(self, n)
        createBottomLeftTabWidget(self, title)
        self.worker.update_process.connect(self.createBottomRightGroupBox())
        self.createProgressBar()

        # styleComboBox.activated[str].connect(self.changeStyle)
        # self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        # disableWidgetsCheckBox.toggled.connect(self.topFirstGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.topSecondGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        # topLayout = QHBoxLayout()
        # topLayout.addWidget(styleLabel)
        # topLayout.addWidget(styleComboBox)
        # topLayout.addStretch(1)
        # topLayout.addWidget(self.useStylePaletteCheckBox)
        # topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        # mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topFirstGroupBox, 1, 0)
        mainLayout.addWidget(self.topSecondGroupBox, 1, 1)
        mainLayout.addWidget(self.topThirdGroupBox, 1, 2)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)



        # self.setWindowTitle("Styles")
        # self.changeStyle('Windows')

    # def changeStyle(self, styleName):
    #     QApplication.setStyle(QStyleFactory.create(styleName))
    #     self.changePalette()

    # def changePalette(self):
    #     if (self.useStylePaletteCheckBox.isChecked()):
    #         QApplication.setPalette(QApplication.style().standardPalette())
    #     else:
    #         QApplication.setPalette(self.originalPalette

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

    def createBottomRightGroupBox(self, data):
        self.bottomRightGroupBox = QGroupBox()
        # self.bottomRightGroupBox.setCheckable(True)
        # self.bottomRightGroupBox.setChecked(True)

        # lineEdit = QLineEdit('s3cRe7')
        # lineEdit.setEchoMode(QLineEdit.Password)

        # spinBox = QSpinBox(self.bottomRightGroupBox)
        # spinBox.setValue(50)

        # dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        # dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        # slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        # slider.setValue(40)

        # scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        # scrollBar.setValue(60)

        # dial = QDial(self.bottomRightGroupBox)
        # dial.setValue(30)
        # dial.setNotchesVisible(True)

        # layout = QGridLayout()
        # layout.addWidget(lineEdit, 0, 0, 1, 2)
        # layout.addWidget(spinBox, 1, 0, 1, 2)
        # layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        # layout.addWidget(slider, 3, 0)
        # layout.addWidget(scrollBar, 4, 0)
        # layout.addWidget(dial, 3, 1, 2, 1)
        # layout.setRowStretch(5, 1)

        # self.bottomRightGroupBox.setLayout(layout)
        self.bottomRightGroupBox.setStyleSheet("background-color: white;")

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)

class WorkerThread(QThread):
    update_process = pyqtSignal(dict)
    def run(self):
        while True:
            line = ser.readline().decode('utf-8')
            print(line)
            if len(line) > 0:
                AnalyzeData(line, data)
                self.update_process.emit({"NodeID":data['NodeID'], "SensorID":data['SensorID'], "value":data['value']})
            print(data['NodeID'], data['SensorID'], data['value'])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_win = QMainWindow()
    main_win.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon_app.png")))
    main_win.setWindowTitle("Agriculture System")
    main_win.setStyleSheet("background-color: #000C66;") 
    main_win.setCentralWidget(WidgetGallery())

    desktop = QDesktopWidget()
    available_geometry = desktop.availableGeometry() 
    
    main_win.setGeometry(available_geometry)
    main_win.show() 

    sys.exit(app.exec_()) """