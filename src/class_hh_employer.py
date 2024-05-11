import requests
import json

class HHEmployer:
    """
    Класс для получения данных компании с сайта hh.ru
    При объявлении класса необходимо ввести id компании
    """
    def __init__(self, id_employer:str):
        self.id_employer = id_employer
        self.url = 'https://api.hh.ru/employers/' + self.id_employer
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_data_employer(self):
        """
        Метод get_data_employer возвращает словарь json с данными компании
        """
        response = requests.get(self.url, self.headers)
        result = response.json()
        return result
