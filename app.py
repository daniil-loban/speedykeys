from sys import argv, exit
from PySide6.QtWidgets import *
from src.layouts.main import Window

if __name__ == "__main__":
    app = QApplication(argv)
    window = Window()
    window.show()
    exit(app.exec())