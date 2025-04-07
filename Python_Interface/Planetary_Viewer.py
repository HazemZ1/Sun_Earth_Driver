# Requirements/Specification
# 1. Live feed of camera looking at the month marker on the Lego
# 2. Drop down selection menu to select month, from January to December
# 3. Live info on time, date, and move speed (move speed can be fed from Arduino)
# 4. Integration with YOLO or OCR to read off the month and provide live feedback, not just reading the pre-set. Also to provide information with the Arduino

# Future Additions
    # Status Changes
    # Electrical/Monitoring Characteristcs 


import sys
import serial
from serial import Serial
import time
from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QComboBox,
    QPushButton,
    QSpinBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase

try:
    arduino = serial.Serial(port="COM9", baudrate=115200)
    print("Serial connection established on COM9 at 115200 baud.")
except serial.SerialException as e:
    print(f"Failed to establish serial connection: {e}")

# arduino.flush()  # Removed to avoid clearing necessary data before writing commands



class PlanetViewer(QMainWindow):
    def __init__(self):
        super().__init__()

         # Window Setup
        self.setWindowTitle("Planetary Viewer")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(1280, 720)

        # Title
        title_label = QLabel("Planet Watcher")
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFixedHeight(40)

        # Camera Feed
        camera_feed = QLabel("Camera Feed")
        camera_feed.setObjectName("cameraFeed")
        camera_feed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Drop-down menu
        self.month_combobox = QComboBox()
        self.month_combobox.setObjectName("monthSelect")
        self.month_combobox.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        self.month_combobox.activated.connect(self.month_select)

        # Start-Stop Button
        self.startButton = QPushButton()
        self.startButton.setCheckable(True)
        self.startButton.setObjectName("startButton")
        self.startButton.setText("Start/Stop")
        self.startButton.clicked.connect(self.start_func)


        # Feedback Box
        self.userfeedback = QLabel()
        self.userfeedback.setObjectName("feedbackBox")
        init_text = "Select a Month, Current Selection: " + self.month_combobox.currentText()
        self.userfeedback.setText(init_text)

        # Status Box
        
        current_time = time.localtime()  # Get struct_time object
        formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", current_time)

        self.status_updates = QLabel()
        self.status_updates.setText(formatted_time)
        self.status_updates.setObjectName("statusBox")

        # Layouts
        gridLayout = QGridLayout()
        gridLayout.addWidget(title_label,0,0,2,2,Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(self.month_combobox,1,1,Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(self.startButton,2,1,Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(self.status_updates,3,1,Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(camera_feed,1,0,2,1,Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(self.userfeedback,4,1,Qt.AlignmentFlag.AlignCenter)
        
        # Define widget and set it
        widget = QWidget()
        widget.setLayout(gridLayout)
        self.setCentralWidget(widget)



    # Start/Stop Functiom
    def start_func(self):
        # Check if the Start/Stop button is toggled on
        if self.startButton.isChecked():
            month = self.month_combobox.currentText() + "\n"
            dispString ="Moving to: " + month
            self.userfeedback.setText(dispString)
            time.sleep(0.1)
            arduino.write(month.encode())
            time.sleep(0.2)
            print("Motion Starting")
        else:
            stop_command = "Stop\n"
            time.sleep(0.1)
            arduino.flush()
            arduino.write(stop_command.encode())
            time.sleep(0.2)
            print("Stopped Moving")


    def month_select(self):
        init_text = "Current Selection: " + self.month_combobox.currentText()
        self.userfeedback.setText(init_text)
        test = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanetViewer()
    window.show()

    # Load and apply QSS stylesheet
    style_path = "Python_Interface/resources/stylesheet.qss"
    with open(style_path, "r") as f:
        app.setStyleSheet(f.read())

    app.exec()
