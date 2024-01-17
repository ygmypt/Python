class Person:
    def __init__(self, last_name, first_name, middle_name):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
 
person1 = Person("Иванов", "Иван", "Иванович")

print(person1.get_full_name()) 
