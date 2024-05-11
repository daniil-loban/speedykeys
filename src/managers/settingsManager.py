import json
import os
from pathlib import Path


class SettingsManager():
    def __init__(self, filename = 'config.json') -> None:
        self.filename = filename
        self.open()

    def open(self):
        with open(self.filename, 'r', encoding='utf-8') as openfile:
            self.settings = json.load(openfile)

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, ensure_ascii=False, indent=4)

    def get_text_style(self):
        s = self.settings['textStyle']
        return f'''
            background-color: {s['background-color']};
            color: {s['color']};
            font: {s['fontSize']} "{s['fontFamily']}";
            {'font-weight: bold;' if s['fontBold'] else ''}
            {'font-style: italic;' if s['fontItalic'] else ''}
            {'text-decoration: underline' if s['fontUnderline'] else ''}
        '''
    
    def get_formatted_text(self, text, cursor_pos):
        begin_style, current_style, end_style = self.get_text_parts_styles()
        begin = text[0:cursor_pos]
        current = text[cursor_pos: cursor_pos +1]      
        end = text[cursor_pos+1:]
        return f'<span {begin_style}>{begin}</span>' \
        f'<span {current_style}>{current}</span>' \
        f'<span {end_style}>{end}</span>'

    def make_text_part_styles(self, color, decoration):
        s = self.settings['selectStyle']
        td = f"text-decoration: {s[decoration]}" if s[decoration] else ''
        return f'style="color: {s[color]};{td}"'
    
    def get_text_parts_styles(self):
        return (
            self.make_text_part_styles('previousTextColor', 'previousTextDecoration'),
            self.make_text_part_styles('currentTextColor','currentTextDecoration'),
            self.make_text_part_styles('nextTextColor', 'nextTextDecoration')
        )

    def get_language(self):
        return self.settings['language']

    def set_language(self, language):
        self.settings['language'] = language

    def get_all_languages(self):
        lang_dir = os.listdir(os.fspath(Path(__file__).resolve().parents[1] / 'lang' ))
        lang_files = filter(lambda s: s[-3:] == '.qm',  lang_dir)
        return map(lambda s: s[:-3], lang_files)  

    def get_font(self):
        s = self.settings['textStyle']
        return (s['fontFamily'], s['fontSize'])
    
    def set_font(self, font_family, font_size):
        s = self.settings['textStyle']
        s['fontSize'] =  font_size
        s['fontFamily'] = font_family

    def get_text_cursor_width(self):
        return self.settings['textStyle']['cursorWidth']
    
    def set_text_cursor_width(self, size=3):
        self.settings['textStyle']['cursorWidth'] = size

    def get_text_background_color(self):
        return self.settings['textStyle']['background-color']

    def set_text_background_color(self, color='rgb(255,255,255)'):
        self.settings['textStyle']['background-color'] = color

    def get_previous_text_color(self):
        return self.settings['selectStyle']['previousTextColor']

    def get_current_text_color(self):
        return self.settings['selectStyle']['currentTextColor']

    def get_next_text_color(self):
        return self.settings['selectStyle']['nextTextColor']

    def set_previous_text_color(self, color):
        self.settings['selectStyle']['previousTextColor'] = color

    def set_current_text_color(self, color):
        self.settings['selectStyle']['currentTextColor'] = color

    def set_next_text_color(self, color):
        self.settings['selectStyle']['nextTextColor'] = color
