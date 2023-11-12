import psycopg2


def create_db(params: dict) -> None:
    """
    Функция для создания БД
    """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute('CREATE DATABASE employers')
    conn.close()


def create_tables(params: dict) -> None:
    """
    Функция для создания таблиц employers и vacancies
    """
    conn = psycopg2.connect(**params)
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute('CREATE TABLE employers (employer_id int PRIMARY KEY,'
                    'company_name varchar(50) NOT NULL, main_city varchar(50), description text);')

        cur.execute('CREATE TABLE vacancies (vacancy_id int PRIMARY KEY, employer_id int REFERENCES employers(employer_id),'
                    'vacancy_name varchar(100) NOT NULL, area varchar(50), salary_from int, '
                    'salary_to int, status varchar(20), publication_date date, vacancy_url text,'
                    'CONSTRAINT chk_vacancies_open CHECK (status in (\'open\', \'closed\', \'direct\')));')
    conn.close()
