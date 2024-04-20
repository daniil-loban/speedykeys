from sys import argv, exit
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle('Speedykeys')
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.layout = QGridLayout(self.centralwidget)
        self.textedit = QTextEdit(self.centralwidget) 
        self.textedit.setObjectName(u"textedit")
        self.textedit.setStyleSheet('''
            #textedit {
                background-color: #FF7F50;
                color: #0000CD;
                font: 16pt "Lato";
            }
        ''')

        self.textedit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.layout.addWidget(self.textedit, 1, 1)
        self.textedit.setFocus()

        text = 'Все началось со статьи Snow Fall. The Avalanche at Tunnel Creek, опубликованной в 2012 году журналом The New York Times. Интерактивная история о нескольких горнолыжниках, погребенных под снегом из-за схода лавины в горах США, мгновенно набрала невиданную популярность. Через неделю после публикации главный редактор The New York Times Джилл Абрамсон отчитывалась о 2,9 млн. визитов, и 3,5 млн. просмотрах страниц. На пике 22,000 пользователей читали статью единовременно. На прочтение читатели тратили примерно 12 минут, часто дольше. В 2020 статья не выглядит ошеломляющей, за это время появилось много проектов: более сложных технически, более разнообразных в подаче. Первыми в публикации мультимедийного материала The New York Times тоже не были. Почему Snow Fall? Несмотря на технологические фокусы, ключевым в истории был качественный текст. Обогащенный дополнительными материалами — фото, видео, комментариями текст превратился в отличный контент. К нему добавили 3D модель гор и завывания вьюги — получили очень эмоциональный эффект присутствия.'
        index = 50
        before = text[0:index]
        after = text[index:]
        self.textedit.append(f"""<span style='color:yellow'>{before}</span>{after}""")

        cursor = self.textedit.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.textedit.setTextCursor(cursor)