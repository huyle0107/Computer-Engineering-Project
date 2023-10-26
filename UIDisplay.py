import sys
import os

from ListNodeBox import *
from ListSensorBox import *
from TopThirdGroupBox import *
from TableData import *

from PyQt5.QtGui import QCursor, QPixmap, QIcon, QFont
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog, QMainWindow, QDesktopWidget)

n = 3

title_watermonitoring = ["Temperature", "Salinity", "EC", "ORP"]
title_soilmonitoring = ["Temperature", "Humidity", "PH", "EC", "N", "P", "K"]
title_airmonitoring = ["Temperature", "Humidity", "Lux", "CO2"]
title = [title_watermonitoring, title_soilmonitoring, title_airmonitoring]


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

        createTopFirstGroupBox(self, n)
        createTopSecondGroupBox(self, n)
        createTopThirdGroupBox(self, n)
        createBottomLeftTabWidget(self, title)
        self.createBottomRightGroupBox()
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
    #         QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

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
    main_win.setStyleSheet("background-color: #000C66;") 
    main_win.setCentralWidget(WidgetGallery())

    desktop = QDesktopWidget()
    available_geometry = desktop.availableGeometry() 
    
    main_win.setGeometry(available_geometry)
    main_win.showFullScreen() 
    sys.exit(app.exec_())