from .settingsManager import SettingsManager


text = 'Все началось со статьи Snow Fall. The Avalanche at Tunnel Creek, опубликованной в 2012 году журналом The New York Times. Интерактивная история о нескольких горнолыжниках, погребенных под снегом из-за схода лавины в горах США, мгновенно набрала невиданную популярность. Через неделю после публикации главный редактор The New York Times Джилл Абрамсон отчитывалась о 2,9 млн. визитов, и 3,5 млн. просмотрах страниц. На пике 22,000 пользователей читали статью единовременно. На прочтение читатели тратили примерно 12 минут, часто дольше. В 2020 статья не выглядит ошеломляющей, за это время появилось много проектов: более сложных технически, более разнообразных в подаче. Первыми в публикации мультимедийного материала The New York Times тоже не были. Почему Snow Fall? Несмотря на технологические фокусы, ключевым в истории был качественный текст. Обогащенный дополнительными материалами — фото, видео, комментариями текст превратился в отличный контент. К нему добавили 3D модель гор и завывания вьюги — получили очень эмоциональный эффект присутствия.'

class TextManager():
    def __init__(self, text=text) -> None:
        self.set_text(text)

    def set_text(self, text):
        self.cursor_pos = 0
        self.text = text

    def get_text(self):
        return text

    def get_cursor_pos(self):
        return self.cursor_pos

    def get_current_char(self):
        return self.text[self.cursor_pos: self.cursor_pos+1]       

    def increment_pos(self):
        if (self.cursor_pos < len(self.text)):
            self.cursor_pos += 1
