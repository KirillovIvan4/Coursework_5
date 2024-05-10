from src import class_hh_employer, class_postgres
from config import host,user,password, db_name
import psycopg2

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

# Объявление класса PostgreSQL
postgres = class_postgres.PostgreSQL(host,user,password,db_name)
# Создание таблици employers
##postgres.create_table_employers()
# Заролнение таблици employers данными
for employer in dict_id_employers:

    empl = class_hh_employer.HHEmployer(dict_id_employers[employer])
    id = str(empl.get_data_employer()['id'])
    name = str(empl.get_data_employer()['name'])
    area = str(empl.get_data_employer()['area']['name'])
    open_vacancies = str(empl.get_data_employer()['open_vacancies'])
    site_url = str(empl.get_data_employer()['site_url'])
    alternate_url = str(empl.get_data_employer()['alternate_url'])
    vacancies_url = str(empl.get_data_employer()['vacancies_url'])
    postgres.insert_data_into_table(id,name,area,open_vacancies,site_url,alternate_url,vacancies_url)
print("Данные о компаниях загдуженны")



