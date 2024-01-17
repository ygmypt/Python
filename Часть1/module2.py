word = input("Введите слово на английском: ")
modified_word = word.replace('x', 'y')
print("Измененное слово:", modified_word)
import random
random_numbers = [random.randint(1, 100) for _ in range(15)]
print("Случайные числа:", random_numbers)
result = 1
for num in random_numbers:
    if num % 3 == 0 and num % 5 == 0:
        result *= num
print("Произведение чисел, кратных 3 и 5:", result)
sentence = input("Введите предложение на английском: ")
modified_sentence = sentence.replace('x', 'y')
print("Измененное предложение:", modified_sentence)
