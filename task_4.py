from get_request import get_request


def get_ip():
    """
    возвращает текущий публичный IP-адрес компьютера в случае удачного запроса к ресурсу https://api.ipify.org,
    иначе возвращет 0
    """
    response = get_request('https://api.ipify.org')
    if response:
        return response.content.decode('utf8')
    return 0


if __name__ == '__main__':
    answer = get_ip()
    if answer:
        print(answer)
