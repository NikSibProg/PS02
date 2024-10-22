import requests

# URL API для получения постов с фильтрацией по userId
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}  # Параметр запроса

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Выводим статус-код ответа
print(f"Status Code: {response.status_code}")

# Выводим содержимое ответа в формате JSON (полученные записи)
if response.status_code == 200:  # Если запрос успешен
    posts = response.json()
    for post in posts:
        print(post)  # Выводим каждую запись
else:
    print("Ошибка при получении данных")
