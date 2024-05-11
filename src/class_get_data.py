import json

class GetData:
    """
    Класс получает данные из файла
    """
    def __init__(self):
        pass

    def get_data_employers(self):
        """
        Метод получает данные из файла employers.json
        :return: Возвращает список со словарями данных компаний
        """
        with open("data/employers.json", "r", encoding='utf-8') as json_data:
            data = json.load(json_data)
        return data