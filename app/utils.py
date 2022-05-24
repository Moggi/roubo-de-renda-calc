import decimal
from decimal import Decimal
from typing import Union


def round_money(amount: Decimal) -> Decimal:
    """Utility function to round money

    Examples
    --------
    >>> round_money(Decimal("0.1551"))
    Decimal('0.15')
    >>> round_money(Decimal("0.1555"))
    Decimal('0.15')
    >>> round_money(Decimal("0.1556"))
    Decimal('0.16')
    """
    decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
    return min(round((amount), 2), round(round(amount, 3), 2))


def get_inss_tax(salary: Union[Decimal, str, int, float], inss_range_rate: dict[str, str] = None) -> Decimal:
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
    Decimal('90.00')
    >>> get_inss_tax("1212")
    Decimal('90.90')
    >>> get_inss_tax("1212.89")
    Decimal('90.98')
    >>> get_inss_tax("1212.90")
    Decimal('90.98')
    >>> get_inss_tax("1300")
    Decimal('98.82')
    >>> get_inss_tax("8070")
    Decimal('828.38')
    """
    salary = Decimal(salary)
    default_range_rate = {
        "1212.00": "7.5",
        "2427.35": "9",
        "3641.03": "12",
        "7087.22": "14",
    }
    final_range_rate = inss_range_rate or default_range_rate
    final_range_rate["-0.01"] = final_range_rate["-0.01"] if "-0.01" in final_range_rate else "0"

    inss_range = sorted(list(map(Decimal, final_range_rate.keys())))
    inss_rate = sorted(list(map(Decimal, final_range_rate.values())))

    residual = 0
    for index in range(1, len(inss_range)):
        range_value = inss_range[index]
        range_tax = inss_rate[index]

        lower_range = inss_range[index - 1] + Decimal("0.01")

        if salary <= range_value:
            if lower_range == Decimal("0.01"):
                lower_range = Decimal("0")

            partial = (salary - lower_range) * range_tax / Decimal("100")
            residual += round_money(partial)
            break

        partial = (range_value - lower_range) * range_tax / Decimal("100")
        residual += round_money(partial)

    final = round_money(residual)
    return final
