import requests

# URL API для поиска репозиториев на GitHub с кодом на HTML
url = 'https://api.github.com/search/repositories'
params = {'q': 'language:html'}  # Параметр поиска

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Выводим статус-код ответа
print(f"Status Code: {response.status_code}")

# Выводим содержимое ответа в формате JSON
if response.status_code == 200:  # Если запрос успешен
    print(response.json())
else:
    print("Ошибка при получении данных")
