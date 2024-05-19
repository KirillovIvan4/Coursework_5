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

    def get_data_employer(self,id_employer):
        """
        Метод get_data_employer возвращает словарь json с данными компании
        """
        url = 'https://api.hh.ru/employers/' + id_employer
        response = requests.get(url, self.headers)
        result = response.json()
        return result, id_employer

    def get_data_vacancies(self,id_employe):
        # params = {'text': 'МТС', 'page': 0, 'per_page': 100}
        url = 'https://api.hh.ru/vacancies?employer_id=' + id_employe
        response = requests.get(url, self.headers,params = {'page': 0, 'per_page': 100})
        result = response.json()
        return result, id_employe
