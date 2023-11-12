from classes.DB_MANAGER import DBManager
from utils import funcs, filing_db_script

EMPLOYER_IDS = (1740, 1057, 78638, 3529, 3127, 80, 39305, 872178, 2180, 139, 26624, 35065)


def main():
    # Задаю параметры для подключения к БД
    params = {'host': 'localhost', 'user': 'postgres', 'password': 'Linch_1563_cool', 'port': '5432'}
    # Создаю БД и таблицы для работодателей и вакансий
    funcs.create_db(params)
    params['dbname'] = 'employers'
    funcs.create_tables(params)

    # Заполняю таблицу данными о работодателях
    for employer_id in EMPLOYER_IDS:
        filing_db_script.filing_employers_table(employer_id, params)

    # Заполняю таблицу данными о вакансиях
    filing_db_script.filing_vacancies_table(EMPLOYER_IDS, params)

    # Методы класса DBManager
    db_manager = DBManager(params)
    print(db_manager.get_companies_and_vacancies_count())

    print(db_manager.get_all_vacancies())

    print(db_manager.get_avg_salary())

    print(db_manager.get_vacancies_with_higher_salary())

    print(db_manager.get_vacancies_with_keyword('python'))


if __name__ == '__main__':
    main()
