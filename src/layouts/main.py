from sys import argv, exit
from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..managers.textManager import TextManager
from ..managers.layoutManager import apply_ui

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        apply_ui(self, 'mainwindow.ui')
        self.text_manager = TextManager()
        self.setup_textedit(self.findChild(QWidget, "textEdit") )
  
    @QtCore.Slot()
    def on_actionOpen_triggered(self):
        print('TODO: load text')

    @QtCore.Slot()
    def on_actionQuit_triggered(self):
        quit()

    def setup_textedit(self, widget):
        self.textedit = widget
        self.textedit.setObjectName(u"textedit")
        self.textedit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.textedit.setFocus()
        self.textedit.setText(self.text_manager.get_formatted_text())
        self.stylize_textedit()
        self.move_cursor(0)

    def stylize_textedit(self):
        self.textedit.setCursorWidth(3)
        self.textedit.setStyleSheet('''
            #textedit {                   
                background-color: #FF7F50;
                color: #0000CD;
                font: 16pt "Lato";
            }
        ''')
        
    @QtCore.Slot()
    def on_textEdit_textChanged(self):
        textA = self.textedit.toPlainText()
        textB = self.text_manager.get_text()
        cur_pos = self.text_manager.cursor_pos
        if len(textA) > len(textB):
            if cur_pos < len(textB) and textA[cur_pos] == textB[cur_pos]:
                self.text_manager.increment_pos()
                self.textedit.setText(self.text_manager.get_formatted_text())
                self.move_cursor(cur_pos + 1)
            else:
                self.textedit.setText(self.text_manager.get_formatted_text())
                self.move_cursor(cur_pos)
        elif len(textA) < len(textB):
            self.textedit.setText(self.text_manager.get_formatted_text())
            self.move_cursor(cur_pos)

    def move_cursor(self, pos=0):
        cursor = self.textedit.textCursor()
        cursor.setPosition(pos)
        self.textedit.setTextCursor(cursor)