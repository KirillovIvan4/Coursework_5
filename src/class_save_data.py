from src import class_hh_employer
import json
class SaveData:
    """
    Клас для сохранения данных в файл
    """
    def __init__(self):
        self.employers = []
        self.employer = {}

    def save_employers(self,dict_id_employers):
        """
        Метод сохраняет данные компаний в файл
        :param dict_id_employers: Словарь со списком компаний состоящий из названия компании (ключ) и ее id (значение)
        """
        for key_employer in dict_id_employers:
            self.employer = {}
            employer = class_hh_employer.HHEmployer(dict_id_employers[key_employer])
            data_employer_in_json = employer.get_data_employer()
            for key_data_employer in ['id', 'name', 'area', 'open_vacancies',
                                      'site_url', 'alternate_url', 'vacancies_url']:
                self.employer[key_data_employer] = data_employer_in_json[key_data_employer]
            self.employers.append(self.employer)

        with open("data/employers.json", "w", encoding='utf-8') as file:
            json.dump(self.employers, file, ensure_ascii=False, indent=4)