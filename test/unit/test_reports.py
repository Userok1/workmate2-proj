import pytest
from src.reports import ClickbaitReport, ReportFactory
from src.utils import YTVideoData


class TestClickbaitReport:
    def test_generate_success(
        self, report_generator: ClickbaitReport, yt_data: list[YTVideoData]
    ):
        headers, table_data = report_generator.generate(yt_data)
        assert headers == ["title", "ctr", "retentaion_rate"]
        assert table_data == [
            ("Как я неделю не мыл кружку и выгорел", 23.0, 25.0),
            ("Проснулся в 5 утра и закрыл спринт", 17.0, 36.0),
        ]

    def test_empty_yt_data(self, report_generator: ClickbaitReport, empty_yt_data):
        headers, table_data = report_generator.generate(empty_yt_data)
        assert headers == ["title", "ctr", "retentaion_rate"]
        assert table_data == []

    def test_filters(self, report_generator: ClickbaitReport, not_passing_filters_rows):
        headers, table_data = report_generator.generate(not_passing_filters_rows)
        assert headers == ["title", "ctr", "retentaion_rate"]
        assert table_data == []

    def test_rows_sorted(
        self, report_generator: ClickbaitReport, yt_data_multiple_files
    ):
        headers, table_data = report_generator.generate(yt_data_multiple_files)
        assert headers == ["title", "ctr", "retentaion_rate"]
        assert table_data == report_generator._sort(table_data)

    def test_sorting(self, report_generator: ClickbaitReport, yt_data_multiple_files):
        headers, table_data = report_generator.generate(yt_data_multiple_files)
        assert report_generator._sort(table_data) == [
            ("Секрет который скрывают тимлиды", 25.0, 22.0),
            ("Как я неделю не мыл кружку и выгорел", 23.0, 25.0),
            ("Как я спал по 4 часа и ничего не понял", 22.5, 28.0),
            ("Я бросил IT и стал фермером", 18.2, 35.0),
            ("Проснулся в 5 утра и закрыл спринт", 17.0, 36.0),
        ]

    def test_sorting_empty_rows(self, report_generator: ClickbaitReport, empty_yt_data):
        headers, table_data = report_generator.generate(empty_yt_data)
        assert report_generator._sort(table_data) == []


class TestReportFactory:
    def test_create_report_generator_success(self):
        rg = ReportFactory.create_report_generator("clickbait")
        assert isinstance(rg, ClickbaitReport)

    def test_report_generator_not_available(self):
        with pytest.raises(ValueError) as e:
            ReportFactory.create_report_generator("notexists")
            assert str(e) == "Unknown report type: notexists"
