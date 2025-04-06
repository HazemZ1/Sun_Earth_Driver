# Requirements/Specification
# 1. Live feed of camera looking at the month marker on the Lego
# 2. Drop down selection menu to select month, from January to December
# 3. Live info on time, date, and move speed (move speed can be fed from Arduino)
# 4. Integration with YOLO or OCR to read off the month and provide live feedback, not just reading the pre-set. Also to provide information with the Arduino

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
    QPushButton,
    QSpinBox,
    QGridLayout,
)

from PyQt6.QtCore import Qt

from PyQt6.QtGui import QFont, QFontDatabase



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

        # Status Box
        self.status_updates = QLabel("Current month,\nmoving speed,\ncurrent date and time")
        self.status_updates.setObjectName("statusBox")
        self.status_updates.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layouts
        right_side = QVBoxLayout()
        right_side.addWidget(self.month_combobox)
        right_side.addWidget(self.status_updates)
        right_side.addStretch()

        main_layout = QHBoxLayout()
        main_layout.addWidget(camera_feed, 2)
        main_layout.addLayout(right_side, 1)

        outer_layout = QVBoxLayout()
        outer_layout.addWidget(title_label)
        outer_layout.addLayout(main_layout)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(outer_layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanetViewer()
    window.show()

    # Load and apply QSS stylesheet
    style_path = "Python_Interface/resources/stylesheet.qss"
    with open(style_path, "r") as f:
        app.setStyleSheet(f.read())

    app.exec()
