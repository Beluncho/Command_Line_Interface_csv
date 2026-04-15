import csv


def read_csv_files(files_list):
    """

    :param files_list: список путей к файлам, например ['data/stats1.csv', 'data/stats2.csv']
    :return: список словарей, где каждый словарь — одно видео
    """
    all_videos = []

    for file_path in files_list:
        print(f'Читаю файл: {file_path}')

        with open(file_path, 'r', encoding='utf-8') as f:
            # DictReader сам использует первую строку как заголовки
            reader = csv.DictReader(f)
            for video in reader:
                all_videos.append(video)

    return all_videos