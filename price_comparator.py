from typing import List

from pydantic import BaseModel, root_validator


class OperatorError(Exception):
    pass


class Operator(BaseModel):
    name: str
    area_codes: List[int]
    rates: List[float]

    @root_validator(pre=True)
    @classmethod
    def same_amount_of_rates_and_area_codes(cls, values):
        if len(values["area_codes"]) != len(values["rates"]):
            raise OperatorError("Different amounts of area codes and rates")
        return values


def convert_operator_info(operators: List[Operator]) -> dict:
    """Converts all operator rates to a single dict with area code and lowest rate"""
    result = {}
    for operator in operators:
        for area_code, rate in zip(operator.area_codes, operator.rates):
            if lower_rate_already_exists(result, area_code, rate):
                continue
            result[str(area_code)] = {"name": operator.name, "rate": rate}
    return result


def compare_rates_from_operators(rates: dict, number: int) -> dict:
    """Returns the lowest operator rate"""
    area_code = find_longest_possible_area_code(rates, number)

    if not area_code:
        return "Number is not callable"

    cheapest = rates[area_code]
    return f"{cheapest['name']}: {cheapest['rate']}"


def find_longest_possible_area_code(rates: dict, number: int) -> str:
    """Returns the longest possible area code from rates if exists, else empty string"""
    longest_area_code = str(number)
    while not longest_area_code in rates and not len(longest_area_code) == 0:
        longest_area_code = longest_area_code[:-1]

    return longest_area_code


def lower_rate_already_exists(res: dict, area_code: int, rate: float) -> bool:
    return str(area_code) in res and res[str(area_code)]["rate"] < rate
