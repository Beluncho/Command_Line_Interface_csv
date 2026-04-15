class ClickbaitReport:
    """Отчёт о кликбейтных видео: кликабельность > 15% и удержание < 40%"""

    def select_suitable(self, videos):
        """
        Выборка подходящих видео
        :param videos: all_videos
        :return: список кликбейтных видео
        """
        result = []
        for video in videos:
            click_rate = float(video['ctr'])
            watch_rate = float(video['retention_rate'])

            if click_rate > 15 and watch_rate < 40:
                result.append(video)
        return result

    def sort_by_click_rate(self, videos):
        """
        :param videos: кликбеййтные видео
        :return: Сортирует видео по убыванию кликабельности
        """
        if not videos:
            return []

        items = []
        for video in videos:
            click_rate = float(video['ctr'])
            items.append((click_rate, video))

        items.sort(reverse=True)

        result = []
        for click_rate, video in items:
            result.append(video)

        return result

    def get_columns(self):
        """
        :return: Какие колонки показывать в итоговой таблице
        """
        return ['title', 'ctr', 'retention_rate']


"""
если понадобится усложнить проект, добавить отчет по другим параметрам,
можно REPORTS  и get_report() вынести в отдельный файл, 
и импортировать туда отчеты с параметрами
"""
# "регистрация" отчета
REPORTS = {
    'clickbait': ClickbaitReport,
}


def get_report(report_name):
    """
    :param report_name: -- report report_name
    :return: Создаём объект класса и возвращает
    """
    if report_name not in REPORTS:
        print(f'Ошибка: отчёт "{report_name}" не найден')
        return None

    return REPORTS[report_name]()