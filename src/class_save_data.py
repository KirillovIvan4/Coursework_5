from src import class_hh_employer
import json
class SaveData:
    """
    Клас для сохранения данных в файл
    """
    def __init__(self):
        self.employers = []
        self.employer = {}
        self.vacancies = []
        self.vacancy = {}

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

    def save_vacancies(self,url):
        """
        Метод сохраняет данные компаний в файл
        :param dict_id_employers: Словарь со списком компаний состоящий из названия компании (ключ) и ее id (значение)
        """

        self.vacancy = {}
        save_vacancies = class_hh_employer.HHEmployer("")
        data_vacancies_in_json = save_vacancies.get_data_vacancies(url)

        for vacancy_number in range(len(data_vacancies_in_json['items'])):
            for key_data_employer in ['id', 'name', 'area', 'salary', 'snippet','alternate_url']:
                print(key_data_employer)
                if key_data_employer == 'salary':
                    if key_data_employer['salary'] == None:
                        self.vacancy['salary_from'] = 0
                        self.vacancy['salary_to'] = 0
                    if key_data_employer['salary']['salary_from'] == None:
                        self.vacancy['salary_from'] = 0
                        self.vacancy['salary_to'] = data_vacancies_in_json['items'][vacancy_number]['salary']['salary_to']
                    if key_data_employer['salary']['salary_to'] == None:
                        self.vacancy['salary_from'] = data_vacancies_in_json['items'][vacancy_number]['salary']['salary_from']
                        self.vacancy['salary_to'] = 0
                if key_data_employer == 'snippet':
                    self.vacancy['requirement'] = data_vacancies_in_json['items'][vacancy_number]['snippet']['requirement']
                    self.vacancy['responsibility'] = data_vacancies_in_json['items'][vacancy_number]['snippet']['responsibility']
                else:
                    self.vacancy[key_data_employer] = data_vacancies_in_json['items'][vacancy_number][key_data_employer]
            self.vacancies = [].append( self.vacancy)

        with open("data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)