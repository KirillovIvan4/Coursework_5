import psycopg2


class DBManager:
    def __init__(self, host: str, user: str, password: str, db_name: str):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):
        """
        Метод получает список всех компаний и количество вакансий у каждой компании.
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
                cursor.execute("""SELECT name_employer, open_vacancies FROM employers""")
                data = cursor.fetchall()
                for i in data:
                    print(f"{i[0]} количество вакансий - {i[1]}")

        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()

    def get_all_vacancies(self):
        """
        Метод получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
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
                cursor.execute("""SELECT name_employer, name_vacancy,salary_from, salary_to, currency, alternate_url 
                FROM employers
                INNER JOIN vacancies USING(id_employer)""")
                data = cursor.fetchall()
                for i in data:
                    print(f"""Компания {i[0]} 
                    Вакансия {i[1]} Ссылка на вакансию {i[5]}
                    Зарплата {i[2]} {i[3]}-{i[4]}
______________________________________________________________""")

        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()

    def get_avg_salary(self):
        """
        Метод получает среднюю зарплату по вакансиям.
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
                cursor.execute("""SELECT AVG(average_salary_in_rubles) 
                FROM vacancies
                WHERE average_salary_in_rubles != 0
                """)
                data = cursor.fetchall()
                for i in data:
                    print(f"Средняя зарплата по всем вакансиям у которых указанна зарплата - {round(i[0])}")
        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()

    def get_vacancies_with_higher_salary(self):
        """
        Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
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
                cursor.execute("""SELECT name_vacancy,salary_from, salary_to, currency, alternate_url
                FROM vacancies
                WHERE average_salary_in_rubles > 
                (SELECT AVG(average_salary_in_rubles) 
                 FROM vacancies
                       WHERE average_salary_in_rubles != 0)
                       """)
                data = cursor.fetchall()
                for i in data:
                    print(f"""Вакансия {i[0]} Ссылка на вакансию {i[4]}
            Зарплата {i[1]} {i[2]}-{i[3]}
______________________________________________________________""")
        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()

    def get_vacancies_with_keyword(self, vacancy):
        """
        Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
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

                cursor.execute("""SELECT *
                        FROM vacancies
                        WHERE name_vacancy LIKE '%s' """ % vacancy
                               )
                data = cursor.fetchall()
                for i in data:
                    print(f"""Вакансия {i[0]} Ссылка на вакансию {i[4]}
                Зарплата {i[1]} {i[2]}-{i[3]}
______________________________________________________________""")
        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)
        finally:
            if connection:
                connection.close()
