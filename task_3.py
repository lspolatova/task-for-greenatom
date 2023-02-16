from bs4 import BeautifulSoup
from typing import Tuple
from get_request import get_request


def count_tags_green_atom() -> Tuple[int, int]:
    """
    возвращает количество тегов на главной страние greenatom и сколько из них содержит атрибуты,
    если запрос к странице был успешен, иначе возвращает кортеж 0
    """
    response = get_request('https://greenatom.ru')
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all()
        tags_attr = [x for x in tags if x.attrs]
        return len(tags), len(tags_attr)
    return 0


if __name__ == '__main__':
    answer = count_tags_green_atom()
    if answer:
        print(f'{answer[0]} HTML-тегов в коде главной страницы сайта greenatom.ru,'
              f' {answer[1]} из них содержит атрибуты')
