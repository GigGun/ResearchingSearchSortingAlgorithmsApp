import os
from bs4 import BeautifulSoup


def load_theory_content():
    """
    загружет краткую справку из файла theory_content.html
    возвращает словарь вида:
    {'Название алгоритма':'Краткое описание'}
    
    """
    data_dict = {} # словарь для содержимого

    with open(os.path.join('interface', 'theory_content.html'), encoding='UTF-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # находим заголовки с названиями алгоритмов
        headers = soup.find_all('h3')

        # проходим по всем заголовкам
        for header in headers:
            # Получаем текст заголовка как ключ
            key = header.get_text(strip=True)

            # Находим следующий элемент после заголовка
            next_element = header.find_next_sibling()

            # собираем весь текст до следующего h3
            content = []
            while next_element and next_element.name != 'h3':
                # Добавляем текст элемента, очищая от лишних пробелов
                content.append(next_element.get_text(strip=True))
                next_element = next_element.find_next_sibling()

            # Сохраняем содержимое в словарь
            data_dict[key] = '\n'.join(content)
    return data_dict


# print(load_theory_content())