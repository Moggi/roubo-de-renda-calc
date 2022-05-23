from dotenv import load_dotenv

load_dotenv(override=True)


def get_inss_tax(salary: float, inss_range_rate: dict[float, float] = None) -> float:
    """Utility function to retrieve inss tax based on salary amount.

    Parameters
    ----------
    salary
        The salary amount as float
    inss_range_rate
        A dicitonary with the salary ranges as keys and its percentages as values.

    Examples
    --------
    >>> get_inss_tax(1200)
    90.0
    >>> get_inss_tax(1212)
    90.9
    >>> get_inss_tax(1212.89)
    90.98
    >>> get_inss_tax(1212.90)
    90.98
    >>> get_inss_tax(1300)
    98.82
    """
    default_range_rate = {
        1212.00: 7.5 / 100,
        2427.35: 9 / 100,
        3641.03: 12 / 100,
        7087.22: 14 / 100,
    }
    final_range_rate = inss_range_rate or default_range_rate
    final_range_rate[0] = final_range_rate[0] if 0 in final_range_rate else 0

    inss_range = list(sorted(final_range_rate.keys()))
    inss_rate = list(sorted(final_range_rate.values()))

    residual = 0
    for index in range(1, len(inss_range)):
        range_value = inss_range[index]
        range_tax = inss_rate[index]

        if salary <= range_value:
            residual += (salary - inss_range[index - 1]) * range_tax
            break

        residual += (range_value - inss_range[index - 1]) * range_tax

    return round(residual, 2)
