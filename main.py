from src import class_postgres, class_save_data, class_get_data, class_db_manager, utils
from config import host, user, password, db_name

utils.record_exchange_rates()
#  Словарь с компаниями и их id
dict_id_employers = {
    "МТС": "3776",
    "Сбер": "3529",
    "Авито": "84585",
    "ВТБ": "4181",
    "Газпром": "39305",
    "Билайн": "4934",
    "Яндекс": "1740",
    "Лаборатория Касперского": "1057",
    "VK": "15478",
    "WILDBERRIES": "87021",
}
get_data = class_get_data.GetData()
# Объявление класса PostgreSQL
postgres = class_postgres.PostgreSQL(host, user, password, db_name)
# Объявление класса DBManager
db_manager = class_db_manager.DBManager(host, user, password, db_name)
# Объявление класса SaveData
save = class_save_data.SaveData()
# Создание таблицы employers
postgres.create_table_employers()
postgres.create_table_vacancies()
#  Сохраняю актуальный курс валют
utils.record_exchange_rates()


# save.save_employers(dict_id_employers)
# save.save_vacancies('87021')

data_employers = get_data.get_data_employers()
data_vacancies = get_data.get_data_vacancies()
# Заполнение таблицы employers данными
for employer in data_employers:
    postgres.insert_data_into_table_employers(employer['id'],
                                              employer['name'],
                                              employer['area']['name'],
                                              employer['open_vacancies'],
                                              employer['site_url'],
                                              employer['alternate_url'],
                                              employer['vacancies_url'])

    print(f"Данные о компании {employer['name']} загружены")

# Заполнение таблицы employers данными
for employer in dict_id_employers:
    save.save_vacancies(dict_id_employers[employer])
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
    print(f"Данные о вакансиях компании {employer} загружены")
#
user_answer = False
while user_answer != True:
    user_answer = (input("""Введите 1 для получения списка всех компаний и количества вакансий у каждой компании.
Введите 2 для получения  списка всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
Введите 3 для получения  средней зарплаты по вакансиям.
Введите 4 для получения  списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
Введите 5 для получения  списка всех вакансий, в названии которых содержатся введенное слово
Введите 6 для выхода из программы
"""))
    if user_answer == '1':
        db_manager.get_companies_and_vacancies_count()
        print()
    elif user_answer == '2':
        db_manager.get_all_vacancies()
        print()
    elif user_answer == '3':
        db_manager.get_avg_salary()
        print()
    elif user_answer == '4':
        db_manager.get_vacancies_with_higher_salary()
        print()
    elif user_answer == '5':
        db_manager.get_vacancies_with_keyword(input("Введите слово\n"))
        print()
    elif user_answer == '6':
        user_answer = True
        print("До свидания")
    else:
        print("ВВедите число от 1 до 6")
