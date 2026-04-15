# 📊 Command_Line_Interface_csv
```
CLI приложение для обработки name.csv-файлов с метриками видео.
Отбирает кликбейтные видео (кликабельность > 15%, удержание < 40%) и выводит таблицу.
```

## 🚀 Запуск
```
# Установка зависимостей
pip install -r requirements.txt

# Запуск (один файл)
python main.py --files csv/stats1.csv --report clickbait

# Запуск (несколько файлов)
python main.py --files csv/stats1.csv csv/stats2.csv --report clickbait
```
## 📊 Пример вывода
```
Читаю файл: stats1.csv
Всего загружено видео: 10
----------------------------------------
+----------------------------------------------------+--------------+-------------+
| title                                              |   click_rate |   watch_rate |
+====================================================+==============+=============+
| Секрет который скрывают тимлиды                    |         25.0 |          22 |
| Как я задолжал ревьюеру 1000 строк кода            |         21.0 |          35 |
| Купил джуну макбук и он уволился                   |         19.0 |          38 |
| Я бросил IT и стал фермером                        |         18.2 |          35 |
+----------------------------------------------------+--------------+-------------+
```

## 📁 Формат CSV-файла
```
title,click_rate,watch_rate,views,likes,avg_watch_time
Я бросил IT и стал фермером,18.2,35,45200,1240,4.2
Как я спал по 4 часа,22.5,28,128700,3150,3.1
```

## 🧪 Запуск тестов
```
pytest tests/ -v
```

## 🏗️ Добавление нового отчёта
```
Создать класс в reports.py, унаследовав его от ClickbaitReport (или сделать свой с методами select_suitable, sort_by_click_rate, get_columns)

Добавить класс в словарь REPORTS
```
# 📁 СТРУКТУРА ПРОЕКТА
```text
Command_line_Interface_csv
│
├── report_cli/    
│   ├── main.py 
│   ├── readers.py
│   ├── reports.py
│   │
│   ├── csv/ 
│   │   ├── stats1.csv
│   │   └── stats2.csv
│   │
│   └── tests/       
│       ├── test_readers.py
│       ├── test_reports.py
│       └── __init__.py
│
├── venv/ 
├── requirements.txt  
└── README.md
```

```text
Файл	                Что делает
main.py	                Главный файл, обрабатывает аргументы, выводит таблицу
readers.py	        Читает CSV-файлы
reports.py	        Логика отбора и сортировки
tests/	                Тесты на pytest
requirements.txt	Зависимости
README.md	        Инструкция 
```