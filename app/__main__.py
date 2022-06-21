import logging
from decimal import Decimal

from dotenv import load_dotenv

from app.utils import get_inss_tax, get_irff_tax

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
]
for salary in salaries:
    inss_tax = get_inss_tax(salary=salary)
    base_irff = Decimal(salary) - inss_tax
    irff_tax = get_irff_tax(base_irff)
    liquid = base_irff - irff_tax
    stolen = inss_tax + irff_tax
    logging.warning(
        {
            "Salary": salary,
            "INSS tax": str(inss_tax),
            "IRFF base": str(base_irff),
            "IRFF tax": str(irff_tax),
            "Stolen": str(stolen),
            "Bottom line": str(liquid),
        }
    )
