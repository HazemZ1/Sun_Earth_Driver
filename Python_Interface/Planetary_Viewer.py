# Requirements/Specification
# 1. Live feed of camera looking at the month marker on the Lego
# 2. Drop down selection menu to select month, from January to December
# 3. Live info on time, date, and move speed (move speed can be fed from Arduino)
# 4. Integration with YOLO or OCR to read off the month and provide live feedback, not just reading the pre-set. Also to provide information with the Arduino

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox,
    QVBoxLayout, QHBoxLayout, QGroupBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase
import sys


class PlanetWatcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planet Watcher")
        #self.setStyleSheet(open("stylesheet.css").read())
        self.resize(1920, 1080)
        self.init_ui()

    def init_ui(self):
        # Layouts
        main_layout = QHBoxLayout()
        right_layout = QVBoxLayout()

        # Camera feed placeholder
        self.camera_label = QLabel("Camera Feed")
        self.camera_label.setObjectName("cameraFeed")
        self.camera_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Drop-down month selector
        self.month_combo = QComboBox()
        self.month_combo.setObjectName("monthSelect")
        self.month_combo.addItems([
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])

        # Info display
        self.info_label = QLabel("Current month,\nmoving speed,\ncurrent date and time")
        self.info_label.setObjectName("infoLabel")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to layouts
        right_layout.addWidget(self.month_combo)
        right_layout.addWidget(self.info_label)

        main_layout.addWidget(self.camera_label)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanetWatcher()

    styles_path = "Python_Interface/resources/stylesheet.qss"
    with open(styles_path, "r") as f:
        styles = f.read()
    app.setStyleSheet(styles)
    window.show()
    sys.exit(app.exec())
