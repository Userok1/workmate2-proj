import csv
import sys
import argparse
import logging
from dataclasses import dataclass
from enum import Enum

logging.basicConfig(filename="logs.log", level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class YTVideoData:
    title: str
    ctr: float
    retention_rate: float
    views: int
    likes: int
    avg_watch_time: float


class Headers(Enum):
    TITLE = "title"
    CTR = "ctr"
    RETENTAION_RATE = "retentaion_rate"
    VIEWS = "views"
    LIKES = "likes"
    AVG_WATCH_TIME = "avg_watch_time"


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, choices=["clickbait"], required=True)

    return parser


def get_args() -> tuple[list[str], str]:
    parser = get_parser()
    args = parser.parse_args()
    files = args.files
    report = args.report

    return files, report


def read_files(files: list[str]) -> list[YTVideoData]:
    """
    Function reads data rows from reveived .csv files
    and returns rows
    """
    rows = []
    for f in files:
        try:
            logger.info(f"File {f}")
            with open(f, "r", newline="", encoding="utf-8") as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader)
                for row in csvreader:
                    rows.append(
                        YTVideoData(
                            title=row[0],
                            ctr=float(row[1]),
                            retention_rate=float(row[2]),
                            views=int(row[3]),
                            likes=int(row[4]),
                            avg_watch_time=float(row[5]),
                        )
                    )
        except FileNotFoundError:
            logger.error("File not found")
            sys.exit(-1)

    return rows


if __name__ == "__main__":
    pass
