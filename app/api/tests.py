import requests


def post_api_call(api_url, user_id, user_query):
    headers = {'Content-Type': 'application/json'}
    payload = {
        'user_id': user_id,
        'user_query': user_query
    }

    response = requests.post(api_url, json=payload, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Не удалось декодировать JSON")
            return response.text
    else:
        print(f"Ошибка: {response.status_code}")
        return response.text


# Пример использования
api_url = 'http://localhost:8000/api/v1/check-writing/'
user_id = '12345'
user_query = 'Привет, как дила?'

response = post_api_call(api_url, user_id, user_query)
print(response)
