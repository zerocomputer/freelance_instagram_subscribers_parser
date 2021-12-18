import sys
import json
import instaloader

# Настройки
username = "yodaxeng"
password = r'c*0288WvZU'
output = "result.json"
target = "interfacely"

# Если есть доп аргумент - это Ваша цель
if len(sys.argv) > 1:
    target = sys.argv[1]

# Если вы передаёте ещё один доп. аргумент, тогда 1-й это так же цель, а второй - это файл, в который нужно записать результат
if len(sys.argv) > 2:
    output = sys.argv[2]

# Инициализация и авторизация
L = instaloader.Instaloader()
L.login(username, password)

# Получаем нужный профиль
profile = instaloader.Profile.from_username(L.context, target)

print(profile)

# Парсим подписчиков
follow_list = []
count = 0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    print("+ subscriber")

# Записываем в JSON формате в нужный файл
follow_list_json = json.dumps(
    {
        "target": target,
        "followers": follow_list
    }
)

file = open(output, "w")
file.write(follow_list_json)
file.close()