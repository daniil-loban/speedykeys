import PySide6.QtWidgets

class Plugin():
    def __init__(self, window, callback=None):
        self.correctCount = 0
        self.incorrectCount = 0
        self.statusBar = window.findChild(PySide6.QtWidgets.QStatusBar, u"statusBar")
        self.label = PySide6.QtWidgets.QLabel()
        self.label.setText(self.formatText())
        self.label.repaint()
        self.statusBar.addWidget(self.label)
        if (callback):
            callback(self)

    def formatText(self):
        return f'<font color=lightgreen><strong>{self.correctCount}</strong></font> \
/ <font color=#f14c4c><strong>{self.incorrectCount}</strong></font>'


    def name(self):
        return 'Counter' 

    def destroy(self):
        self.statusBar.removeWidget(self.label)

    def reset(self):
        self.count = 0

    def action(self, data):
        char, isCorrect = data 
        if isCorrect:
            self.correctCount += 1
        else:
            self.incorrectCount +=1
        self.label.setText(self.formatText())
        self.label.repaint()
