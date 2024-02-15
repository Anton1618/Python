'''
pyttsx3 - библиотека преобразования текста в речь на Python

'''
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Скорость речи
engine.setProperty('voice', 'ru')  # Русский язык

text = input('Введите текст для произнесения: ')
engine.say(text)
engine.runAndWait()
