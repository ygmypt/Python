users = {}

def создать_пользователя(логин, пароль):
    if логин not in users:
        users[логин] = пароль
        print("Пользователь успешно создан.")
    else:
        print("Этот логин уже занят.")

def вход(логин, пароль):
    if логин in users and users[логин] == пароль:
        print("Вход выполнен успешно.")
    else:
        print("Неправильный логин или пароль.")

создать_пользователя("user1", "password1")
создать_пользователя("user2", "password2")

вход("user1", "password1")  
вход("user1", "wrongpassword") 
