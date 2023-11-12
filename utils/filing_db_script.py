from classes.HH_API import HhApiWorker
import psycopg2


def filing_employers_table(employer_id, params: dict) -> None:
    """
    Функция заполняющая таблицу employers данными
    """
    hh_worker = HhApiWorker()
    conn = psycopg2.connect(**params)
    conn.autocommit = True

    with conn.cursor() as cur:
        employer_info = hh_worker.get_employer_info(employer_id)
        right_employer_info = [employer_info['id'], employer_info['name'], employer_info['area']['name'],
                               employer_info['description']]
        cur.execute('INSERT INTO employers VALUES (%s, %s, %s, %s)', (right_employer_info[:]))

    conn.close()


def filing_vacancies_table(employer_ids, params: dict) -> None:
    """
    Функция заполняющая таблицу vacancies данными
    """
    hh_worker = HhApiWorker()
    conn = psycopg2.connect(**params)
    conn.autocommit = True

    with conn.cursor() as cur:
        for emp_id in employer_ids:
            vacancies_list = hh_worker.get_employer_vacancies(emp_id)
            for vacancie in vacancies_list:
                right_vacancie_info = [vacancie['id'], emp_id, vacancie['name'], vacancie['area']['name'],
                                       vacancie['salary']['from'], vacancie['salary']['to'], vacancie['type']['id'],
                                       vacancie['published_at'], vacancie['url']]

                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (right_vacancie_info[:]))

    conn.close()
