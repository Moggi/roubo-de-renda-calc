import logging
import sys

from dotenv import load_dotenv

from app.utils import get_tax_summary

load_dotenv(override=True)

salaries = [
    "2000",
    "2500",
    "2800",
    "3000",
    "3400",
    "3800",
    "4000",
    "4400",
    "4900",
    "5000",
    "5300",
    "6000",
    "7000",
    "8000",
    "9000",
]


if __name__ == "__main__":
    salaries = sys.argv[-1:] if len(sys.argv) > 1 else salaries

    for salary in salaries:
        summary = get_tax_summary(salary=salary)
        logging.warning(summary)
