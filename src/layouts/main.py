from sys import argv, exit
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..managers.textManager import TextManager

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.text_manager = TextManager()
        self.setWindowTitle('Speedykeys')
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.layout = QGridLayout(self.centralwidget)
        self.textedit = QTextEdit(self.centralwidget)
        self.setup_textedit()
        self.layout.addWidget(self.textedit, 1, 1)
        self.move_cursor(0)
        self.textedit.setFocus()
        self.textedit.setText(self.text_manager.get_formatted_text())
    
    def setup_textedit(self):
        self.textedit.textChanged.connect(self.changed)
        self.textedit.setObjectName(u"textedit")
        self.textedit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.stylize_textedit()

    def stylize_textedit(self):
        self.textedit.setCursorWidth(3)
        self.textedit.setStyleSheet('''
            #textedit {
                caret-color: white;                    
                background-color: #FF7F50;
                color: #0000CD;
                font: 16pt "Lato";
            }
        ''')

    def changed(self):
        textA = self.textedit.toPlainText()
        textB = self.text_manager.get_text()
        cur_pos = self.text_manager.cursor_pos
        if len(textA) != len(textB):
            self.textedit.setText(self.text_manager.get_formatted_text())
            if cur_pos < len(textB) and textA[cur_pos] == textB[cur_pos]:
                self.text_manager.increment_pos()
                self.move_cursor(cur_pos + 1)
            else:
                self.move_cursor(cur_pos)

    def move_cursor(self, pos=0):
        cursor = self.textedit.textCursor()
        cursor.setPosition(pos)
        self.textedit.setTextCursor(cursor)