import json


def json_file(filename):
    """
    Загружаем json фаил
    :param : filename имя файла
    :return: получаем обрабатанный фаил
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        filename = json.load(file)
        return filename


def sort_data(state, dict_data):
    """
    Сортируем даные, state переменная для отбора файла
    в данной случае, прошел или не прошел перевод средств
    :param : state переменная отбора
    :param : dict_data словарь из которого получаем данные
    :return: получаем обрабатанный словарь
    """
    executed = []
    for data in dict_data:
        if data.get("state") == state:
            executed.append(data)
    return executed


def sort_by_date(data):
    """
    Сортировка по дате транзакции от ближайщей
    """
    data.sort(key=lambda x: x['date'], reverse=True)
    return data


def convert_date(date):
    """
    Замена даты с 2000-10-10 на 10.10.2000
    """
    date = date[:10]
    date = date.split("-")
    new_date = f'{date[2]}.{date[1]}.{date[0]}'
    return new_date


def bankcard_number(number):
    """
    Замены нужных цифр банковской карты на звездочки
    """
    new_card_number = f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    return new_card_number


def account_number(acc_number):
    """
    Получение последних 6 знаков счет, где первый две звездочки
    """
    new_acc_number = f'**{acc_number[-4:]}'
    return new_acc_number
