import pytest

from src.reports import ClickbaitReport
from src.utils import read_files


@pytest.fixture
def single_table_data():
    csv_t1_data = (
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Проснулся в 5 утра и закрыл спринт,17.0,36,38700,980,4.1\n"
        "Как я неделю не мыл кружку и выгорел,23.0,25,213400,6700,2.8\n"
        "Дедлайн подкрался незаметно,10.0,70,25600,670,7.5\n"
    )
    return csv_t1_data


@pytest.fixture
def multiple_tables_data(single_table_data):
    csv_t2_data = (
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Я бросил IT и стал фермером,18.2,35,45200,1240,4.2\n"
        "Как я спал по 4 часа и ничего не понял,22.5,28,128700,3150,3.1\n"
        "Почему сеньоры не носят галстуки,9.5,82,31500,890,8.9\n"
        "Секрет который скрывают тимлиды,25.0,22,254000,8900,2.5\n"
    )
    return single_table_data, csv_t2_data


@pytest.fixture
def bad_table_data():
    # Число 45200.9 должно быть целым
    csv_bad_data = (
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Я бросил IT и стал фермером,18.2,35,45200.9,1240,4.2\n"
        "Как я спал по 4 часа и ничего не понял,22.5,28,128700,3150,3.1\n"
        "Почему сеньоры не носят галстуки,9.5,82,31500,890,8.9\n"
        "Секрет который скрывают тимлиды,25.0,22,254000,8900,2.5\n"
    )
    return csv_bad_data


@pytest.fixture
def single_file(tmp_path, single_table_data):
    t1_file = tmp_path / "table_1.csv"
    t1_file.write_text(single_table_data, encoding="utf-8")
    return str(t1_file)


@pytest.fixture
def multiple_files(tmp_path, multiple_tables_data):
    t1_table = tmp_path / "table_1.csv"
    t2_table = tmp_path / "table_2.csv"
    t1_table.write_text(multiple_tables_data[0], encoding="utf-8")
    t2_table.write_text(multiple_tables_data[1], encoding="utf-8")
    return str(t1_table), str(t2_table)


@pytest.fixture
def bad_file(tmp_path, bad_table_data):
    bad_table = tmp_path / "bad_table.csv"
    bad_table.write_text(bad_table_data, encoding="utf-8")
    return str(bad_table)


@pytest.fixture
def empty_file(tmp_path):
    empty_table = tmp_path / "bad_table.csv"
    empty_table.write_text("", encoding="utf-8")
    return str(empty_table)


@pytest.fixture
def only_headers_file(tmp_path):
    only_headers_string = "student,date,coffee_spent,sleep_hours,study_hours,mood,exam"
    table_only_headers = tmp_path / "only_headers_table.csv"
    table_only_headers.write_text(only_headers_string, encoding="utf-8")
    return str(table_only_headers)


@pytest.fixture
def report_generator():
    return ClickbaitReport()


@pytest.fixture
def yt_data(single_file):
    files = [single_file]
    rows = read_files(files)
    return rows


@pytest.fixture
def yt_data_multiple_files(multiple_files):
    files = [multiple_files[0], multiple_files[1]]
    rows = read_files(files)
    return rows


@pytest.fixture
def empty_yt_data():
    return []


@pytest.fixture
def not_passing_filters_yt_data():
    data = (
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Дедлайн подкрался незаметно,10.0,70,25600,670,7.5\n"
        "Почему сеньоры не носят галстуки,9.5,82,31500,890,8.9\n"
    )
    return data


@pytest.fixture
def not_passing_filters_file(tmp_path, not_passing_filters_yt_data):
    file = tmp_path / "table.csv"
    file.write_text(not_passing_filters_yt_data, encoding="utf-8")
    return str(file)


@pytest.fixture
def not_passing_filters_rows(not_passing_filters_file):
    files = [not_passing_filters_file]
    rows = read_files(files)
    return rows
