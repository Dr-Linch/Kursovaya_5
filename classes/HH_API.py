import requests


class HhApiWorker:
    """
    Класс для работы с API HH
    """

    def get_employer_id(self, company_name: str):
        """
        Получает название компании и возвращает id работодателя с большим количеством открытых вакансий
        :param company_name: Название компании
        :return: id работодателя
        """
        params = {'text': company_name, 'sort_by': 'by_vacancies_open', 'only_with_vacancies': True}
        url = 'https://api.hh.ru/employers'
        response = requests.get(url, params)
        employee_json = response.json()
        return employee_json['items'][0]

    def get_employer_info(self, employee_id: str):
        """
        Получает id работодателя и возвращает данные о нём
        :param employee_id: id работодателя
        :return: Возвращает данные о работодателе в json формате
        """
        params = {'employer_id': employee_id, }
        url = f'https://api.hh.ru/employers/{employee_id}'
        response = requests.get(url, params)
        employee_info = response.json()
        return employee_info

    def get_employer_vacancies(self, employee_id: str):
        """
        Получает id работодателя и возвращает список доступных вакансий
        :param employee_id: id работодателя
        :return: список вакансий
        """
        params = {'employer_id': employee_id, 'page': 0, 'per_page': 50, 'only_with_salary': True}
        url = f'https://api.hh.ru/vacancies?employer_id={employee_id}'
        response = requests.get(url, params)
        vacancies = response.json()
        page = 0
        while page < 4:
            page += 1
            params = {'employer_id': employee_id, 'page': page, 'per_page': 50, 'only_with_salary': True}
            response = requests.get(url, params)
            response_data = response.json()
            vacancies['items'].extend(response_data['items'])
        return vacancies['items']
