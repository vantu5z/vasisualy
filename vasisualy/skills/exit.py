from ..core import speak
import random

trigger = ("Пока", "пока", "Прощай", "прощай", "До свидания", "до свидания", "Прощайте", "прощайте", "Удачи", "удачи", "Бывай", "бывай", "До встречи", "до встречи", "Увидимся", "увидимся", "Выход", "выход", "Exit", "exit")

def main(say):
    for i in trigger:
        if i == say:
            bye = random.choice(("Пока, мой друг.", "Пока, товарищ.", "До встречи.", "Прощай.", "До свидания.", "Не покидай меня!", "Очень жаль расставаться с тобой."))
            speak.tts_d.speak(bye)
            speak.tts_d.close()
            exit()
            
    return ""
