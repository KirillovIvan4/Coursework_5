from src import class_hh_employer,utils
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

    def save_vacancies(self, id_employer):
        """
        Метод сохраняет данные компаний в файл
        :param dict_id_employers: Словарь со списком компаний состоящий из названия компании (ключ) и ее id (значение)
        """
        self.vacancies = []
        save_vacancies = class_hh_employer.HHEmployer("")
        data_vacancies_in_json, id_employer = save_vacancies.get_data_vacancies(id_employer)

        for vacancy_number in range(len(data_vacancies_in_json['items'])):
            vacancies = data_vacancies_in_json['items'][vacancy_number]
            self.vacancy = {}
            self.vacancy['id_employer'] = id_employer
            # Перебираю ключи вакансии которые буду записывать
            for key_data_employer in ['id_vacancy', 'name', 'area', 'salary', 'snippet', 'alternate_url']:
                if key_data_employer == 'id_vacancy':
                    self.vacancy['id_vacancy'] = vacancies['id']
                elif key_data_employer == 'area':
                    self.vacancy['area'] = vacancies['area']['name']
                elif key_data_employer == 'salary':
                    if vacancies['salary'] == None:
                        self.vacancy['salary_from'] = 0
                        self.vacancy['salary_to'] = 0
                        self.vacancy['currency'] = 'RUR'
                        self.vacancy['average_salary_in_rubles'] = 0
                    elif vacancies['salary']['from'] == None:
                        # Если зарплаты "от" нет, то приравниваю ее к 0
                        # salary_from = 0
                        #
                        self.vacancy['salary_from'] = 0
                        self.vacancy['salary_to'] = vacancies['salary']['to']
                        self.vacancy['currency'] = vacancies['salary']['currency']
                        self.vacancy['average_salary_in_rubles'] = utils.get_average_salary_in_rubles(self.vacancy['salary_from'],
                                                                                                      self.vacancy['salary_to'],
                                                                                                      self.vacancy['currency'])
                    elif vacancies['salary']['to'] == None:
                        # Если зарплаты "до" нет, то приравниваю ее к зарплате от
                        self.vacancy['salary_from'] = vacancies['salary']['from']
                        self.vacancy['salary_to'] = vacancies['salary']['from']
                        self.vacancy['currency'] = vacancies['salary']['currency']
                        self.vacancy['average_salary_in_rubles'] = utils.get_average_salary_in_rubles(self.vacancy['salary_from'],
                                                                                                      self.vacancy['salary_to'],
                                                                                                      self.vacancy['currency'])
                    else:
                        self.vacancy['salary_from'] = vacancies['salary']['from']
                        self.vacancy['salary_to'] = vacancies['salary']['to']
                        self.vacancy['currency'] = vacancies['salary']['currency']
                        self.vacancy['average_salary_in_rubles'] = utils.get_average_salary_in_rubles(self.vacancy['salary_from'],
                                                                                                      self.vacancy['salary_to'],
                                                                                                      self.vacancy['currency'])

                elif key_data_employer == 'snippet':
                    self.vacancy['requirement'] = vacancies['snippet'][
                        'requirement']
                    self.vacancy['responsibility'] = vacancies['snippet'][
                        'responsibility']
                else:
                    self.vacancy[key_data_employer] = vacancies[key_data_employer]
            self.vacancies.append(self.vacancy)

                # else:
                #     break
        with open("data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
