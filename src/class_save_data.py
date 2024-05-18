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

    def save_vacancies(self, url):
        """
        Метод сохраняет данные компаний в файл
        :param dict_id_employers: Словарь со списком компаний состоящий из названия компании (ключ) и ее id (значение)
        """

        self.vacancy = {}
        save_vacancies = class_hh_employer.HHEmployer("")
        data_vacancies_in_json = save_vacancies.get_data_vacancies(url)

        for vacancy_number in range(len(data_vacancies_in_json['items'])):
            print(data_vacancies_in_json['items'][vacancy_number]['salary'])
            for key_data_employer in ['id', 'name', 'area', 'salary', 'snippet', 'alternate_url']:
                #print(data_vacancies_in_json['items'][vacancy_number]['salary'])
                if key_data_employer == 'salary':
                    if data_vacancies_in_json['items'][vacancy_number]['salary'] == None:
                        self.vacancy['salary_from'] = 0
                        self.vacancy['salary_to'] = 0
                    elif data_vacancies_in_json['items'][vacancy_number]['salary']['from'] == None:
                        self.vacancy['salary_from'] = 0
                        self.vacancy['salary_to'] = data_vacancies_in_json['items'][vacancy_number]['salary']['to']
                    elif data_vacancies_in_json['items'][vacancy_number]['salary']['to'] == None:
                        self.vacancy['salary_from'] = data_vacancies_in_json['items'][vacancy_number]['salary']['from']
                        self.vacancy['salary_to'] = 0
                if key_data_employer == 'snippet':
                    self.vacancy['requirement'] = data_vacancies_in_json['items'][vacancy_number]['snippet'][
                        'requirement']
                    self.vacancy['responsibility'] = data_vacancies_in_json['items'][vacancy_number]['snippet'][
                        'responsibility']
                else:
                    self.vacancy[key_data_employer] = data_vacancies_in_json['items'][vacancy_number][key_data_employer]
            self.vacancies = [].append(self.vacancy)
            print("_____________________________")
        with open("data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
    # def save_vacancies(self,url):
    #     """
    #     Метод сохраняет данные компаний в файл
    #     :param dict_id_employers: Словарь со списком компаний состоящий из названия компании (ключ) и ее id (значение)
    #     """
    #     self.vacancies = []
    #     save_vacancies = class_hh_employer.HHEmployer("")
    #     data_vacancies_in_json = save_vacancies.get_data_vacancies(url)
    #
    #     for vacancy_number in range(len(data_vacancies_in_json['items'])):
    #         data_vacancies = data_vacancies_in_json['items'][vacancy_number]
    #         self.vacancy = {}
    #         for key_data_employer in ['id', 'name', 'area', 'salary', 'snippet','alternate_url']:
    #             if key_data_employer == 'area':
    #                 self.vacancy['area'] = data_vacancies['area']['name']
    #
    #             elif key_data_employer == 'salary':
    #                 if data_vacancies[key_data_employer] == None:
    #                     self.vacancy['salary_from'] = 0
    #                     self.vacancy['salary_to'] = 0
    #                 else:
    #                     self.vacancy['currency'] = data_vacancies['salary']['currency']
    #                     if data_vacancies['salary']['from'] == None:
    #                         self.vacancy['salary_from'] = 0
    #                         self.vacancy['salary_to'] = data_vacancies['salary']['to']
    #                     elif data_vacancies['salary']['to'] == None:
    #                         self.vacancy['salary_from'] = data_vacancies['salary']['from']
    #                         self.vacancy['salary_to'] = 0
    #                     else:
    #                         self.vacancy['salary_from'] = data_vacancies['salary']['from']
    #                         self.vacancy['salary_to'] = data_vacancies['salary']['to']
    #
    #             elif key_data_employer == 'snippet':
    #                 self.vacancy['requirement'] = data_vacancies['snippet']['requirement']
    #                 self.vacancy['responsibility'] = data_vacancies['snippet']['responsibility']
    #             else:
    #                 self.vacancy[key_data_employer] = data_vacancies[key_data_employer]
    #         self.vacancies.append( self.vacancy)
    #     print('-----------------------------------------------------------')
    #     with open("data/vacancies.json", "w", encoding='utf-8') as file:
    #         json.dump(self.vacancies, file, ensure_ascii=False, indent=4)