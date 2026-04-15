import pytest
import tempfile
import csv
import os
from readers import read_csv_files


def test_read_single_file():
    """Чтение одного файла"""
    # Создаём временный CSV-файл
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as tmp:
        tmp.write('title,click_rate,watch_rate\n')
        tmp.write('Видео 1,20,30\n')
        tmp.write('Видео 2,10,50\n')
        tmp_path = tmp.name

    try:
        videos = read_csv_files([tmp_path])
        assert len(videos) == 2
        assert videos[0]['title'] == 'Видео 1'
        assert videos[0]['click_rate'] == '20'
    finally:
        os.remove(tmp_path)


def test_read_multiple_files():
    """Чтение нескольких файлов"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as tmp1:
        tmp1.write('title,click_rate,watch_rate\n')
        tmp1.write('Видео 1,20,30\n')
        path1 = tmp1.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as tmp2:
        tmp2.write('title,click_rate,watch_rate\n')
        tmp2.write('Видео 2,25,35\n')
        path2 = tmp2.name

    try:
        videos = read_csv_files([path1, path2])
        assert len(videos) == 2
    finally:
        os.remove(path1)
        os.remove(path2)


def test_file_not_found():
    """Ошибка при чтении несуществующего файла"""
    with pytest.raises(FileNotFoundError):
        read_csv_files(['not_exists.csv'])
