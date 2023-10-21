""" import tkinter as tk
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



    
     window.mainloop() """

import sys
import os

from PyQt5.QtGui import QCursor, QPixmap, QIcon, QFont
from PyQt5.QtCore import QDateTime, Qt, QTimer
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

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        # styleComboBox.activated[str].connect(self.changeStyle)
        # self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        # disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
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
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
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
    #         QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox()

        n = 3

        radioButton = list()

        for i in range(n):
            
            k = QRadioButton(f"Server mã {i + 1}")
            radioButton.append(k)
        
        # radioButton[0].setChecked(True)

        layout = QVBoxLayout()
        layout.setSpacing(10)  # Set the spacing between widgets to zero

        # # Add an empty widget as spacing at the top
        # top_spacer = QWidget()
        # top_spacer.setFixedHeight(10)  # Adjust the height to control the spacing
        # layout.addWidget(top_spacer)

        title_spacer = QWidget()
        title_spacer.setFixedHeight(65)  # Adjust the height to control the spacing
        # Create a QLabel and set its text
        label = QLabel("Các sever đang hoạt động")
        label.setFont(QFont("Arial", 30))
        # Add the QLabel to the QWidget
        label.setParent(title_spacer)
        layout.addWidget(title_spacer)

        for j in range(n):
            layout.addWidget(radioButton[j])
        layout.addStretch(1)
        
        self.topLeftGroupBox.setLayout(layout)
        self.topLeftGroupBox.setStyleSheet(
            "background-color: white;"
            "margin-left: 20px;"
            "border-radius: 20px;"  # Adjust the radius as needed
            )

    def createTopRightGroupBox(self):    
        self.topRightGroupBox = QGroupBox()

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)

        self.topRightGroupBox.setLayout(layout)
        self.topRightGroupBox.setStyleSheet(
                        "background-color: white;"
                        "border-radius: 10px;"  # Adjust the radius as needed
                        # "border: 0.5px solid black;"  # Adjust the border color and width as needed
                        )

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Hello\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")
        self.bottomLeftTabWidget.setStyleSheet("background-color: white;")

    def createBottomRightGroupBox(self):
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


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_win = QMainWindow()
    main_win.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon_app.png")))
    main_win.setWindowTitle("Agriculture System")
    main_win.setStyleSheet("background-color: blue;") 
    main_win.setCentralWidget(WidgetGallery())

    desktop = QDesktopWidget()
    available_geometry = desktop.availableGeometry()
    
    main_win.setGeometry(available_geometry)
    main_win.show()
    sys.exit(app.exec_())