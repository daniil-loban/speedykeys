from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ...managers.settingsManager import SettingsManager
from ...managers.textManager import TextManager
from ...managers.layoutManager import apply_ui


class CustomTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(CustomTextEdit, self).__init__(parent)
        self.settings = SettingsManager()
        self.text_manager = TextManager()
        self.textChanged.connect(self.onTextChanged)
        self.setup_textedit(self)
        self.stylize_textedit()

    def setup_textedit(self, widget):
        widget.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.text_redraw()
        widget.move_cursor(0)

    def text_redraw(self):
        text = self.text_manager.get_text()
        cur_pos = self.text_manager.get_cursor_pos()
        self.setText(self.settings.get_formatted_text(text, cur_pos))

    def stylize_textedit(self, settings=None):
        self.settings = settings if settings != None else self.settings
        self.setCursorWidth(self.settings.get_text_cursor_width())
        self.setStyleSheet(self.settings.get_text_style())
        cur_pos = self.text_manager.get_cursor_pos()
        self.text_redraw()
        self.move_cursor(cur_pos)
        self.setFocus()

    def onTextChanged(self):
        textA = self.toPlainText()
        textB = self.text_manager.get_text()
        isRecursionExit = len(textA) == len(textB)
        if isRecursionExit: return
        cur_pos = self.text_manager.get_cursor_pos()
        isIncorrectPos = cur_pos + 1 != self.textCursor().position()
        isDeletedText = len(textA) < len(textB)
        isCorrectEnter = not isIncorrectPos and textA[cur_pos] == textB[cur_pos]
        
        if isIncorrectPos or isDeletedText: 
            self.text_redraw()
            self.move_cursor(cur_pos)
        
        elif isCorrectEnter:
            self.text_manager.increment_pos()
            self.text_redraw()
            self.move_cursor(cur_pos + 1)

    def move_cursor(self, pos=0):
        cursor = self.textCursor()
        cursor.setPosition(pos)
        self.setTextCursor(cursor)