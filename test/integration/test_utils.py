import pytest
import logging

from src.utils import read_files, get_parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestReadFiles:
    def test_one_file(self, single_file):
        files = [single_file]
        table_data = read_files(files)
        assert isinstance(table_data, list)
        for row in table_data:
            assert len(vars(row).values()) == 6
        assert len(table_data) == 3
        row = table_data[0]
        assert (
            row.title,
            row.ctr,
            row.retention_rate,
            row.views,
            row.likes,
            row.avg_watch_time,
        ) == ("Проснулся в 5 утра и закрыл спринт", 17.0, 36, 38700, 980, 4.1)

    def test_multiple_files(self, multiple_files):
        files = [multiple_files[0], multiple_files[1]]
        table_data = read_files(files)
        assert isinstance(table_data, list)
        assert len(table_data) == 7
        row = table_data[3]
        assert (
            row.title,
            row.ctr,
            row.retention_rate,
            row.views,
            row.likes,
            row.avg_watch_time,
        ) == ("Я бросил IT и стал фермером", 18.2, 35, 45200, 1240, 4.2)

    def test_bad_data(self, bad_file):
        files = [bad_file]
        with pytest.raises(ValueError) as e:
            logger.error(str(e))
            read_files(files)

    def test_empty_file(self, empty_file):
        files = [empty_file]
        with pytest.raises(StopIteration):
            read_files(files)

    def test_empty_file_with_headers(self, only_headers_file):
        files = [only_headers_file]
        res_dict = read_files(files)
        assert len(res_dict) == 0


class TestGetParser:
    def test_valid_arguments(self, multiple_files):
        parser = get_parser()
        args = parser.parse_args(
            ["--files", multiple_files[0], multiple_files[1], "--report", "clickbait"]
        )
        assert args.files[0] == multiple_files[0]
        assert args.files[1] == multiple_files[1]
        assert args.report == "clickbait"

    def test_files_option_not_provided(self, multiple_files):
        parser = get_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--report", "clickbait"])

    def test_report_option_not_provided(self, multiple_files):
        parser = get_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(
                [
                    "--files",
                    multiple_files[0],
                    multiple_files[1],
                ]
            )

    def test_unrecognised_command(self, multiple_files):
        parser = get_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(
                [
                    "--files",
                    multiple_files[0],
                    multiple_files[1],
                    "--report",
                    "rep",
                    "--invalidcommand",
                    "badarg",
                ]
            )
