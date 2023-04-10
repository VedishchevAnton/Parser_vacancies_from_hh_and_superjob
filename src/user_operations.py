"""Реализация класса с методами для пользователя"""


class UserOperations:
    def __init__(self, vacancies, filter_words=None, top_count=0):
        self.vacancies = vacancies
        self.filter_words = filter_words
        self.top_count = top_count
        self.list_vacancies = []

    def filter_vacancies(self):
        """
        Метод сортировки вакансий по ключевым словам пользователя
        """
        for i in self.vacancies:
            if i['description'] is not None:
                if self.filter_words.lower() in i['description'].lower():
                    self.list_vacancies.append(i)
        return self.list_vacancies

    def sorting(self):
        """
        Метод сортировки вакансий по зарплате
        """
        sorted_data = sorted(self.vacancies, key=lambda x: self.get_avg_salary_range(x['payment']), reverse=True)
        return sorted_data



