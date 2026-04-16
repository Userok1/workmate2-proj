from tabulate import tabulate
import logging

from src.reports import ReportFactory
from src.utils import read_files, get_args

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Reading arguments from terminal...")
    files, report_type = get_args()
    logger.info("Reading files...")
    rows = read_files(files)
    logger.info("Files read successfully")
    logger.info("Creating report generator...")
    report_generator = ReportFactory.create_report_generator(report_type)
    logger.info("Report generator created successfully")
    logger.info("Reports generation...")
    headers, table_data = report_generator.generate(rows)
    print()
    logger.info("Building tabulate table...")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    logger.info("Tabulate table built successfully")


if __name__ == "__main__":
    main()
