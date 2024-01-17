memory = {}

def ответ_да_или_нет(вопрос):
    transformed_question = вопрос.lower().strip()  

    if transformed_question in memory:
        ответ = memory[transformed_question]
        print("Ответ (из памяти):", ответ)
    else:
        ответ = input("Введите ответ на вопрос (\"да\" или \"нет\"): ")
        memory[transformed_question] = ответ 
        print("Ответ:", ответ)

ответ_да_или_нет("Будет ли завтра дождь?")
ответ_да_или_нет("Должен ли я сделать это задание?")
ответ_да_или_нет("Будешь помнить меня завтра?")

print("Запомненные вопросы и ответы:")
for question, answer in memory.items():
    print(question, "-", answer)
