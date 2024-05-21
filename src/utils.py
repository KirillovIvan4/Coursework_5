import json
import requests
def upload_exchange_rates():
    """
    Функция получает курс валют на текущую дату от центробанка
    """
    response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    result = response.json()['rates']
    return result

def record_exchange_rates():
    """
    Функция сохраняет курс валют в файл
    """
    exchange_rates = upload_exchange_rates()
    with open("data/exchange_rates.json", "w", encoding='utf-8') as file:
        json.dump(exchange_rates, file, ensure_ascii=False, indent=4)



def get_dict_exchange_rates():
    """
    Функция считывает json файл c курсом валют и преобразует его список
    """

    with open('data/exchange_rates.json', 'r', encoding='utf-8') as json_exchange_rates:
        exchange_rates = json.load(json_exchange_rates)
        return exchange_rates

def get_average_salary_in_rubles(salary_from, salary_to, currency):
    """
    Функция конвертирует курс валют в рубли"""
    exchange_rates = get_dict_exchange_rates()
    if currency == 'RUR':
        average_salary_in_rubles = int(salary_from + salary_to) /2
        return average_salary_in_rubles
    else:
        if currency == 'BYR':
            salary_from = salary_from / exchange_rates['BYN']
            salary_to = salary_to / exchange_rates['BYN']
            average_salary_in_rubles = int(salary_from + salary_to) / 2
            return average_salary_in_rubles
        else:
            salary_from = salary_from / exchange_rates[currency]
            salary_to = salary_to / exchange_rates[currency]
            average_salary_in_rubles = int(salary_from + salary_to) / 2
            return average_salary_in_rubles