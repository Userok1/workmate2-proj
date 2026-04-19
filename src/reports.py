from abc import ABC, abstractmethod
from typing import Any

from src.utils import YTVideoData, Headers


class BaseYTReport(ABC):
    @abstractmethod
    def generate(
        self, rows: list[YTVideoData]
    ) -> Any:
        pass


class ClickbaitReport(BaseYTReport):
    def generate(
        self, rows: list[YTVideoData]
    ) -> tuple[list[str], list[tuple[str, float, float]]]:
        """
        Function receives a list of YTVideoData objects and returns
        headers and rows for tabulate to process it
        """
        headers = [
            Headers.TITLE.value,
            Headers.CTR.value,
            Headers.RETENTAION_RATE.value,
        ]
        table_rows = []
        for row in rows:
            if row.ctr > 15 and row.retention_rate < 40:
                table_rows.append((row.title, row.ctr, row.retention_rate))
        return headers, self._sort(table_rows)

    def _sort(self, table_rows: list[tuple[str, float, float]]):
        return sorted(table_rows, key=lambda r: r[1], reverse=True)


class ReportFactory:
    _report_generators = {"clickbait": ClickbaitReport}

    @classmethod
    def create_report_generator(cls, report_name: str):
        """
        Method create report generator coressponding to report_name
        """
        report_generator = cls._report_generators.get(report_name)
        if not report_generator:
            raise ValueError(f"Unknown report type: {report_name}")
        return report_generator()
