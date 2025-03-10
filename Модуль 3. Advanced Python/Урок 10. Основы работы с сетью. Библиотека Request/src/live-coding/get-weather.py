import requests



def main():
    url = 'http://api.weatherapi.com/v1/current.json'

    key = "1b6cb79e8dfe4a76aa9151908242907"

    params = {
        'key': key,
        'q':  'London',
        'aqi': 'no'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)
    print(response.json())


if __name__ == '__main__':
    main()
