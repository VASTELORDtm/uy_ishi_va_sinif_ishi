import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QCheckBox, QComboBox, QVBoxLayout, QHBoxLayout
)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        self.label = QLabel("Enter your name:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")
        self.check_box = QCheckBox("I agree to the terms")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])

        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.check_box)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(hbox)
        main_layout.addWidget(self.combo_box)

        self.setLayout(main_layout)

        self.button.clicked.connect(self.on_submit)

        self.setWindowTitle("Simple PyQt6 App")
        self.setGeometry(100, 100, 300, 200)

    def on_submit(self):
        name = self.line_edit.text()
        if self.check_box.isChecked():
            message = f"Hello, {name}! You agreed to the terms."
        else:
            message = f"Hello, {name}! You did not agree to the terms."
        self.label.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
