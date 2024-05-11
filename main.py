from src import class_hh_employer, class_postgres,class_save_data, class_get_data
from config import host,user,password, db_name
import psycopg2
import json

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
##postgres.create_table_employers()

###empl = class_hh_employer.HHEmployer(dict_id_employers["Сбер"])
####empl.get_data_employer()

# save = class_save_employer.SaveData()
# save.save_employers(dict_id_employers)

data = get_data.get_data_employers()

# Заролнение таблици employers данными
for employer in data:
     postgres.insert_data_into_table(employer['id'],
                                    employer['name'],
                                    employer['area']['name'],
                                    employer['open_vacancies'],
                                    employer['site_url'],
                                    employer['alternate_url'],
                                    employer['vacancies_url'])

print("Данные о компаниях загдуженны")




