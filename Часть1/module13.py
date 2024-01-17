my_list = []

def add_unique_below_10(num):
    if num <= 10 and num not in my_list:
        my_list.append(num)
    else:
        print("Число превышает 10 или уже присутствует в списке и не может быть добавлено.")

add_unique_below_10(5)
add_unique_below_10(12)
add_unique_below_10(8)
add_unique_below_10(3)
add_unique_below_10(5)

print(my_list)  # Выведет: [5, 8, 3]
