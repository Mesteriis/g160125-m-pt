import requests


def show_full_response():
    response = requests.get('https://api.github.com')

    print(response.status_code)  # Output: 200
    print(response.headers['content-type'])  # Output: 'application/json; charset=utf-8'
    print(response.url)
    print(response.json())


def show_get_with_params():
    url = 'https://api.github.com/search/repositories?q=python&sort=stars'
    params = {'q': 'python', 'sort': 'stars', 'page': 2}
    response = requests.get('https://api.github.com/search/repositories', params=params)
    print(response.url)  # Output: https://api.github.com/search/repositories?q=python&sort=stars
    print(response.json())  # Output: JSON данные в виде словаря Python


def search_request(search_query: str):
    # URL для поиска в Google
    url = "https://www.google.com/search"

    # Параметры запроса
    params = {
        'q': search_query,
        'hl': 'en',  # Язык интерфейса
        'lr': 'lang_en',  # Язык результатов
        'gl': 'us'  # Регион (например, 'us' для США)
    }

    # Заголовки, чтобы имитировать браузер
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Выполнение GET-запроса
    response = requests.get(url, params=params, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Печать URL запроса
        print(f"Requested URL: {response.url}")
        # Печать содержимого ответа
        print(response.text[:1000])
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")


def main():
    # print('Show full response as json')
    # show_full_response()
    # print('\n\n', '* ' * 15, '\nShow get with params')
    # show_get_with_params()
    #
    # print('\n\n', '* ' * 15, '\nSearch results')
    search_request('python')


if __name__ == '__main__':
    main()
