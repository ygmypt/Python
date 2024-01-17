# Функция для поиска элемента в словаре
def search_in_dictionary(data, key):
    if key in data:
        return data[key]
    else:
        return None

# Функция для поиска элемента в списке
def search_in_list(data, item):
    if item in data:
        return f"Элемент {item} найден в списке на позиции {data.index(item)}"
    else:
        return "Элемент не найден в списке"

# Пример использования функций
dictionary_data = {"name": "Alice", "age": 25, "city": "New York"}
list_data = [10, 20, 30, 40, 50]

print(search_in_dictionary(dictionary_data, "age")) # Поиск элемента в словаре
print(search_in_list(list_data, 30)) # Поиск элемента в списке

from fuzzywuzzy import fuzz

# Функция для выполнения нечеткого сравнения строк
def fuzzy_string_compare(str1, str2):
    similarity_score = fuzz.ratio(str1, str2)
    return similarity_score

# Пример использования функции
string1 = "apple"
string2 = "aple"
score = fuzzy_string_compare(string1, string2)
print("Схожесть строк:", score)
