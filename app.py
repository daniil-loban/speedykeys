from sys import argv, exit
from PySide6 import QtWidgets, QtCore
from src.layouts.main import Window
from src.application import Application

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts, True)
    app = Application(argv)
    window = Window(app)
    window.show()
    exit(app.exec())