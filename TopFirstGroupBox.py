import sys
import os

from PyQt5.QtGui import QCursor, QPixmap, QIcon, QFont
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog, QMainWindow, QDesktopWidget)

def createTopFirstGroupBox(self, n):
    self.topFirstGroupBox = QGroupBox()
    radioButton = list()

    for i in range(n):
        k = QRadioButton(f"Server mã {i + 1}")
        radioButton.append(k)
        
    # radioButton[0].setChecked(True)

    layout = QVBoxLayout()
    layout.setSpacing(10)  # Set the spacing between widgets to zero

    # Add an empty widget as spacing at the top
    top_spacer = QWidget()
    top_spacer.setFixedSize(5, 0)  # Adjust the height to control the spacing
    layout.addWidget(top_spacer)

    title_spacer = QWidget()
    title_spacer.setFixedHeight(65)  # Adjust the height to control the spacing
    # Create a QLabel and set its text
    label = QLabel("Các sever đang hoạt động")
    label.setFont(QFont("Arial", 30))
    label.setStyleSheet("font-weight: bold;")
    # Add the QLabel to the QWidget
    label.setParent(title_spacer)
    layout.addWidget(title_spacer)

    for j in range(n):
        layout.addWidget(radioButton[j])
        # Set the size of the button (width x height)
        radioButton[j].setStyleSheet("QAbstractButton::indicator { width: 40px; height: 40px; }")
        # Set the size of the text
        radioButton[j].setStyleSheet("QRadioButton { font-size: 20px; }")  # Adjust the font size as needed
    layout.addStretch(1)

    layout.setContentsMargins(20, 0, 0, 0)
    self.topFirstGroupBox.setLayout(layout)
    self.topFirstGroupBox.setStyleSheet(
        "background-color: white;"
        "border-radius: 20px;"  # Adjust the radius as needed
        )


