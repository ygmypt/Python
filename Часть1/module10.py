import random

def гадалка():
    варианты_ответов = ["Да", "Нет", "Возможно", "Попробуй еще раз", "Не стоит этого делать", "Скорее всего", "Лучше не рисковать"]
    вопрос = input("Задайте свой вопрос: ")
    ответ = random.choice(варианты_ответов)
    print("Гадалка говорит:", ответ)

гадалка()
