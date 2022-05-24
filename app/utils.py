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
    >>> get_inss_tax("1212.62")
    Decimal('90.95')
    >>> get_inss_tax("1212.63")
    Decimal('90.96')
    >>> get_inss_tax("2427.35")
    Decimal('200.28')
    >>> get_inss_tax("3641.03")
    Decimal('345.92')
    >>> get_inss_tax("8070")
    Decimal('828.38')
    """
    salary = Decimal(salary)
    default_range_rate = {
        "0": "0",
        "1212.00": "7.5",
        "2427.35": "9",
        "3641.03": "12",
        "7087.22": "14",
    }
    final_range_rate = inss_range_rate or default_range_rate

    inss_range = list(map(Decimal, final_range_rate.keys()))
    inss_rate = list(map(Decimal, final_range_rate.values()))

    residual = 0
    for index in range(1, len(inss_range)):
        range_value = inss_range[index]
        range_tax = inss_rate[index]

        lower_range = Decimal("0") if index == 1 else inss_range[index - 1] + Decimal("0.01")

        if salary <= range_value:

            partial = (salary - lower_range) * range_tax / Decimal("100")
            residual += round_money(partial)
            break

        partial = (range_value - lower_range) * range_tax / Decimal("100")
        residual += round_money(partial)

    final = round_money(residual)
    return final


def get_irff_tax(salary: Union[Decimal, str, int, float]) -> Decimal:
    """Utility function to retrieve IRFF tax based on salary.

    Examples
    --------
    >>> get_irff_tax("1000")
    Decimal('0.00')
    >>> get_irff_tax("2473.65")
    Decimal('42.72')
    >>> get_irff_tax("3500.63")
    Decimal('170.29')
    >>> get_irff_tax("4664.68")
    Decimal('413.42')
    >>> get_irff_tax("8000")
    Decimal('1330.64')
    """
    range_rates = {
        "1903.98": ["0", "0"],
        "2826.65": ["7.5", "142.80"],
        "3751.05": ["15", "354.80"],
        "4664.68": ["22.5", "636.13"],
        "Infinity": ["27.5", "869.36"],
    }
    salary = Decimal(salary)
    for range_value, range_rate in range_rates.items():
        irrf_rate = Decimal(range_rate[0]) / Decimal("100")
        irrf_deduction = Decimal(range_rate[1])

        if salary <= Decimal(range_value):
            final = salary * irrf_rate - irrf_deduction
            return round_money(final)
