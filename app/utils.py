import decimal
from decimal import Decimal


def get_inss_tax(salary: str, inss_range_rate: dict[str, str] = None) -> str:
    """Utility function to retrieve inss tax based on salary amount.

    Parameters
    ----------
    salary
        The salary amount as float
    inss_range_rate
        A dicitonary with the salary ranges as keys and its percentages as values.

    Examples
    --------
    >>> get_inss_tax("1200")
    '90.00'
    >>> get_inss_tax("1212")
    '90.90'
    >>> get_inss_tax("1212.89")
    '90.98'
    >>> get_inss_tax("1212.90")
    '90.98'
    >>> get_inss_tax("1300")
    '98.82'
    >>> get_inss_tax("8070")
    '828.38'
    """
    default_range_rate = {
        "1212.00": "7.5",
        "2427.35": "9",
        "3641.03": "12",
        "7087.22": "14",
    }
    final_range_rate = inss_range_rate or default_range_rate
    final_range_rate["-0.01"] = final_range_rate["-0.01"] if "-0.01" in final_range_rate else "0"

    inss_range = list(sorted(final_range_rate.keys(), key=Decimal))
    inss_rate = list(sorted(final_range_rate.values(), key=Decimal))

    decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN

    residual = 0
    for index in range(1, len(inss_range)):
        range_value = inss_range[index]
        range_tax = inss_rate[index]

        lower_range = Decimal(inss_range[index - 1]) + Decimal("0.01")

        if Decimal(salary) <= Decimal(range_value):
            if lower_range == Decimal("0.01"):
                lower_range = Decimal("0")

            partial = (Decimal(salary) - lower_range) * Decimal(range_tax) / Decimal(100)
            residual += round(round(partial, 3), 2)
            break

        partial = (Decimal(range_value) - lower_range) * Decimal(range_tax) / Decimal(100)
        residual += round(round(partial, 3), 2)

    final = round(round(residual, 3), 2)
    return str(final)
