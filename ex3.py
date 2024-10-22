import requests

# URL для POST-запроса
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос
response = requests.post(url, json=data)

# Выводим статус-код ответа
print(f"Status Code: {response.status_code}")

# Выводим содержимое ответа
if response.status_code == 201:  # 201 Created
    print("Данные успешно созданы:")
    print(response.json())  # Выводим содержимое в формате JSON
else:
    print("Ошибка при отправке данных")
