import psycopg2


class DBManager:
    def __init__(self, params):
        self.conn = psycopg2.connect(**params)
        self.conn.autocommit = True

    def get_companies_and_vacancies_count(self):
        """
         Получает список всех компаний и количество вакансий у каждой компании.
        """
        with self.conn.cursor() as cur:
            cur.execute('SELECT employers.employer_id, COUNT(vacancy_id) FROM employers '
                        'JOIN vacancies USING(employer_id) GROUP BY employer_id;')
            queri_resalt = cur.fetchall()
        return queri_resalt

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute('SELECT company_name, vacancy_name, salary_from, vacancy_url FROM vacancies '
                        'JOIN employers USING(employer_id)')
            query_resalt = cur.fetchall()
        return query_resalt

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        with self.conn.cursor() as cur:
            cur.execute('SELECT AVG(salary_from) FROM vacancies')
            query_resalt = cur.fetchall()
        return query_resalt

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with self.conn.cursor() as cur:
            cur.execute('SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies);')
            query_resalt = cur.fetchall()
        return query_resalt

    def get_vacancies_with_keyword(self, key_word: str):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова.
        """
        with self.conn.cursor() as cur:
            cur.execute(f'SELECT * FROM vacancies WHERE vacancy_name LIKE \'%{key_word}%\';')
            query_resalt = cur.fetchall()
        return query_resalt
