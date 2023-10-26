import sys
import os

from PyQt5.QtGui import QCursor, QPixmap, QIcon, QFont
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog, QMainWindow, QDesktopWidget)

def createBottomLeftTabWidget(self, title):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)
        layout = QVBoxLayout()
        layout.setSpacing(10)  # Set the spacing between widgets to zero

        # Add an empty widget as spacing at the top
        top_spacer = QWidget()
        top_spacer.setFixedSize(5, 0)  # Adjust the height to control the spacing
        layout.addWidget(top_spacer)
        title_spacer = QWidget()
        title_spacer.setFixedHeight(65)  # Adjust the height to control the spacing
        # Create a QLabel and set its text
        label = QLabel(f"{title[1][0]} history")
        label.setFont(QFont("Arial", 30))
        label.setStyleSheet("font-weight: bold;")
        # Add the QLabel to the QWidget
        label.setParent(title_spacer)
        layout.addWidget(title_spacer)

        tab1 = QWidget()
        tableWidget = QTableWidget(2, 2)

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