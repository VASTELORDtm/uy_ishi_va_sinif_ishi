import sys
from PyQt6.QtWidgets import  QPushButton  
from PyQt6.QtWidgets import  QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.on_resize = None
        self.setWindowTitle("Hello, PyQt6")
        self.setGeometry(100, 100, 1366, 768)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        button = QPushButton("Click Me")
        layout = QVBoxLayout()
        layout.addWidget(button)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)

   
        self.setWindowTitle("Overlapping Label on Image")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.image_label = QLabel(self)
        pixmap = QPixmap("assets/wings.webp")
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 0, self.width(), self.height())
        self.image_label.setScaledContents(True)

        self.bottom_right_label = QLabel("Bottom Right Label", self)
        self.bottom_right_label.setStyleSheet("color: white; background-color: black; padding: 5px;")
        self.bottom_right_label.adjustSize()

        self.update_label_position()

        self.resizeEvent = self.on_resize

        def update_label_position(self):
            x = self.width() - self.bottom_right_label.width() - 10
            y = self.height() - self.bottom_right_label.height() - 10
            self.bottom_right_label.move(x, y)

        def on_resize(self, event):
            self.image_label.setGeometry(0, 0, self.width(), self.height())
            self.update_label_position()

    def update_label_position(self):
        pass


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        sys.exit(app.exec())



