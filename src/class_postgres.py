import psycopg2
class PostgreSQL:
    """
    Класс для работы с postgresql
    """
    def __init__(self, host:str, user:str, password:str, db_name:str):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def create_table_employers(self):
        """Метод добавляет в PostgreSQL таблицу employers"""
        try:
            # Подключаемся к базе данных
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True
            # Создаем курсор чезез контекстный менеджер with чтобы
            # по завершении работы не было необходимости закрывать его вручную методом cursor.close()
            # Создаем таблицу employers (компании)
            with connection.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE employers(
                    id serial PRIMARY KEY,
                    name varchar(100) NOT NULL,
                    area varchar(100) NOT NULL,
                    open_vacancies smallint NOT NULL,
                    site_url varchar(100) NOT NULL,
                    alternate_url varchar(100) NOT NULL,
                    vacancies_url varchar(100) NOT NULL)"""
                )
        except Exception as _ex:
            return print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()



    def insert_data_into_table_employers(self, id, name, area, open_vacancies, site_url, alternate_url, vacancies_url):
        """
        Метод Добавляет данные о компании в таблицу employers
        :param id: id компании
        :param name: название компании
        :param area: город, где компания находится
        :param open_vacancies: количество открытых вакансий
        :param site_url: ссылка на сайт компании
        :param alternate_url: ссылка на страницу компании на hh.ru
        :param vacancies_url: ссылка на вакансии компании на hh.ru
        """
        d = 'dfgsfg'
        try:
            # Подключаемся к базе данных
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True
            # Добавляем данные о компании в таблицу
            with connection.cursor() as cursor:
                cursor.execute(
                   (id, name, area, open_vacancies, site_url, alternate_url, vacancies_url)
                )


        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()
    def create_table_vacancies(self):
        """Метод добавляет в PostgreSQL таблицу vacancies"""
        try:
            # Подключаемся к базе данных
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True
            # Создаем курсор чезез контекстный менеджер with чтобы
            # по завершении работы не было необходимости закрывать его вручную методом cursor.close()
            # Создаем таблицу employers (компании)
            with connection.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE vacancies(
                    id serial PRIMARY KEY,
                    name varchar(100) NOT NULL,
                    area varchar(100) NOT NULL,
                    salary_from int,
                    salary_to int,
                    currency varchar(1000) NOT NULL,
                    average_salary_in_rubles int,
                    requirement varchar(1000) NOT NULL,
                    responsibility varchar(1000) NOT NULL,
                    alternate_url varchar(100) NOT NULL)"""
                )
        except Exception as _ex:
            return print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()
    def insert_data_into_table_vacancies(self, id, name, area, salary_from, salary_to, currency, average_salary_in_rubles, requirement, responsibility,alternate_url):
        """
        Метод Добавляет данные о компании в таблицу employers
        :param id: id вакансии
        :param name: название вакансии
        :param area: город, где вакансии находится
        :param salary_from: зарплата от
        :param salary_to: зарплата до
        :param currency: валюта
        :param average_salary_in_rubles: средняя зарплата в рублях
        :param requirement:требования
        :param responsibility: обязанности
        :param alternate_url: ссылка на вакансию на hh.ru
        """
        try:
            # Подключаемся к базе данных
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
            connection.autocommit = True
            # Добавляем данные о компании в таблицу
            with connection.cursor() as cursor:
                cursor.execute(
                   """INSERT INTO vacancies (id, name, area, salary_from, salary_to, currency, average_salary_in_rubles, requirement, responsibility,alternate_url) VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                   (id, name, area, salary_from, salary_to, currency, average_salary_in_rubles, requirement, responsibility,alternate_url)
                )


        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()

