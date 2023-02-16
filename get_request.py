import requests


def get_request(url: str):
    """
    функция делает запрос, в случае успеха возвращает ответ на него, иначе 0
    """
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'User Agent for greenatom',
        }
    )
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.ConnectionError as e:
        print('Connection Error')
        print(e)
        return 0
    except requests.HTTPError as e:
        print(e)
        return 0
    return response
