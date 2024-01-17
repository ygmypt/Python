from fuzzywuzzy import fuzz

class Person:
    def __init__(self, full_name, dob, height):
        self.full_name = full_name
        self.dob = dob
        self.height = height

def fuzzy_string_compare(str1, str2):
    similarity_score = fuzz.ratio(str1, str2)
    return similarity_score

people_data = [
    Person("Иванов Иван Иванович", "01.01.1990", 125),
    Person("Петрова Наталья Викторовна", "05.05.1985", 118),
    Person("Сидорова Наташа Петровна", "10.10.2000", 121)
]

def search_by_height(people):
    result = [person for person in people if person.height > 120]
    return result

def search_by_name(name, people):
    result = []
    for person in people:
        if fuzzy_string_compare(person.full_name, name) > 80:
            result.append(person)
    return result

tall_people = search_by_height(people_data)
print("Люди с ростом больше 120:")
for person in tall_people:
    print(person.full_name)

natasha_variants = search_by_name("Наташа", people_data)
print("\nРезультаты нечеткого поиска по имени \"Наташа\":")
for person in natasha_variants:
    print(person.full_name, person.height)

