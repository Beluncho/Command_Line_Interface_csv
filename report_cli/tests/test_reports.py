import pytest
from reports import ClickbaitReport, get_report


@pytest.fixture
def sample_videos():
    """Тестовые видео"""
    return [
        {'title': 'Видео 1', 'click_rate': '20', 'watch_rate': '30'},
        {'title': 'Видео 2', 'click_rate': '10', 'watch_rate': '50'},
        {'title': 'Видео 3', 'click_rate': '25', 'watch_rate': '35'},
        {'title': 'Видео 4', 'click_rate': '18', 'watch_rate': '45'},
        {'title': 'Видео 5', 'click_rate': '16', 'watch_rate': '39'},
    ]


def test_select_suitable(sample_videos):
    """Проверка отбора подходящих видео"""
    report = ClickbaitReport()
    suitable = report.select_suitable(sample_videos)

    # Должны остаться: Видео 1 (20/30), Видео 3 (25/35), Видео 5 (16/39)
    assert len(suitable) == 3

    titles = [v['title'] for v in suitable]
    assert 'Видео 1' in titles
    assert 'Видео 3' in titles
    assert 'Видео 5' in titles
    assert 'Видео 2' not in titles
    assert 'Видео 4' not in titles


def test_sort_by_click_rate(sample_videos):
    """Проверка сортировки по убыванию кликабельности"""
    report = ClickbaitReport()
    suitable = report.select_suitable(sample_videos)
    sorted_videos = report.sort_by_click_rate(suitable)

    # Самый высокий клик (25) должен быть первым
    assert sorted_videos[0]['title'] == 'Видео 3'
    assert float(sorted_videos[0]['click_rate']) == 25

    # Второй (20)
    assert sorted_videos[1]['title'] == 'Видео 1'
    assert float(sorted_videos[1]['click_rate']) == 20

    # Третий (16)
    assert sorted_videos[2]['title'] == 'Видео 5'
    assert float(sorted_videos[2]['click_rate']) == 16


def test_get_columns():
    """Проверка списка колонок"""
    report = ClickbaitReport()
    assert report.get_columns() == ['title', 'click_rate', 'watch_rate']


def test_get_report_success():
    """Получение существующего отчёта"""
    report = get_report('clickbait')
    assert report is not None
    assert isinstance(report, ClickbaitReport)


def test_get_report_fail():
    """Получение несуществующего отчёта"""
    report = get_report('not_exists')
    assert report is None
