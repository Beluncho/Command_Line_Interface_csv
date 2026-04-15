import argparse
import sys
from tabulate import tabulate
from readers import read_csv_files
from reports import get_report


def show_report(report_name, all_videos):
    """Показывает отчёт в виде таблицы"""
    # Получаем объект отчёта
    report = get_report(report_name)
    if report is None:
        return

    # Отбираем подходящие видео
    suitable_videos = report.select_suitable(all_videos)

    # Сортируем по кликабельности
    sorted_videos = report.sort_by_click_rate(suitable_videos)

    # Если ничего не нашлось
    if len(sorted_videos) == 0:
        print('Нет видео, подходящих под условия отчёта')
        return

    # Готовим данные для таблицы
    table_data = []
    for video in sorted_videos:
        row_data = []
        for col in report.get_columns():
            row_data.append(video[col])
        table_data.append(row_data)

    # Выводим красивую таблицу
    print(tabulate(table_data, headers=report.get_columns(), tablefmt='grid'))


def main():
    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Анализ метрик видео на YouTube')

    # Параметр --files (можно указать один или несколько файлов)
    parser.add_argument(
        '--files',
        nargs='+',  # один или несколько аргументов
        required=True,
        help='Пути к CSV-файлам (один или несколько)'
    )

    # Параметр --report
    parser.add_argument(
        '--report',
        required=True,
        help='Название отчёта (сейчас доступен только clickbait)'
    )

    # Разбираем аргументы
    args = parser.parse_args()

    # Читаем данные из файлов
    try:
        all_videos = read_csv_files(args.files)
    except FileNotFoundError as e:
        print(f'Ошибка: файл не найден - {e}')
        sys.exit(1)
    except Exception as e:
        print(f'Ошибка при чтении файлов: {e}')
        sys.exit(1)

    # Проверяем, что данные есть
    if len(all_videos) == 0:
        print('Внимание: файлы не содержат данных')
        sys.exit(0)

    # Показываем статистику
    print(f'Всего загружено видео: {len(all_videos)}')
    print('-' * 40)

    # Показываем отчёт
    show_report(args.report, all_videos)


if __name__ == '__main__':
    main()