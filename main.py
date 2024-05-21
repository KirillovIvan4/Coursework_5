from src import class_hh_employer, class_postgres,class_save_data, class_get_data, utils
from config import host,user,password, db_name
#import psycopg2
import json

utils.record_exchange_rates()

dict_id_employers = {
    "МТС":"3776",
    "Сбер":"3529",
    "Авито":"84585",
    "ВТБ":"4181",
    "Газпром":"39305",
    "Билайн":"4934",
    "Яндекс":"1740",
    "Лаборатория Касперского":"1057",
    "VK":"15478",
    "WILDBERRIES":"87021",
}
get_data = class_get_data.GetData()
# Объявление класса PostgreSQL
postgres = class_postgres.PostgreSQL(host,user,password,db_name)
# Создание таблици employers
postgres.create_table_employers()
postgres.create_table_vacancies()

###empl = class_hh_employer.HHEmployer(dict_id_employers["Сбер"])
####empl.get_data_employer()

save = class_save_data.SaveData()
# save.save_employers(dict_id_employers)
# save.save_vacancies('87021')

data_employers = get_data.get_data_employers()
data_vacancies = get_data.get_data_vacancies()
# Заролнение таблици employers данными
for employer in data_employers:
    postgres.insert_data_into_table_employers(employer['id'],
                                employer['name'],
                                employer['area']['name'],
                                employer['open_vacancies'],
                                employer['site_url'],
                                employer['alternate_url'],
                                employer['vacancies_url'])

print("Данные о компаниях загдуженны")

#Заролнение таблици employers данными
for employers in dict_id_employers:
    save.save_vacancies(dict_id_employers[employers])
    data_vacancies = get_data.get_data_vacancies()
    for vacancies in data_vacancies:
        postgres.insert_data_into_table_vacancies(vacancies['id_vacancy'],
                                                  vacancies['id_employer'],
                                                  vacancies['name'],
                                                  vacancies['area'],
                                                  vacancies['salary_from'],
                                                  vacancies['salary_to'],
                                                  vacancies['currency'],
                                                  vacancies['average_salary_in_rubles'],
                                                  vacancies['requirement'],
                                                  vacancies['responsibility'],
                                                  vacancies['alternate_url'])


    print(f"Данные о вакансиях компани {employers} загдуженны")
#

