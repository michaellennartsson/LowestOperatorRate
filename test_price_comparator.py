import pytest

from price_comparator import (
    compare_rates_from_operators,
    convert_operator_info,
    Operator,
    OperatorError,
)

a = Operator(
    name="Operator_A",
    area_codes=[1, 268, 46, 4620, 468, 4631, 4673, 46732],
    rates=[0.9, 5.1, 0.17, 0, 0.15, 0.15, 0.9, 1.1],
)

b = Operator(
    name="Operator_B", area_codes=[1, 44, 46, 467, 48], rates=[0.92, 0.5, 0.2, 1, 1.2]
)

c = Operator(
    name="Operator_C",
    area_codes=[1, 44, 46, 4678, 48],
    rates=[0.55, 0.6, 0.25, 1.1, 1.6],
)

op_rates = {
    "1": {"name": "Operator_C", "rate": 0.55},
    "268": {"name": "Operator_A", "rate": 5.1},
    "44": {"name": "Operator_B", "rate": 0.5},
    "46": {"name": "Operator_A", "rate": 0.17},
    "4620": {"name": "Operator_A", "rate": 0.0},
    "4631": {"name": "Operator_A", "rate": 0.15},
    "467": {"name": "Operator_B", "rate": 1.0},
    "4673": {"name": "Operator_A", "rate": 0.9},
    "46732": {"name": "Operator_A", "rate": 1.1},
    "4678": {"name": "Operator_C", "rate": 1.1},
    "468": {"name": "Operator_A", "rate": 0.15},
    "48": {"name": "Operator_B", "rate": 1.2},
}


def test_create_operator():
    with pytest.raises(OperatorError):
        a = Operator(
            name="Operator_A",
            area_codes=[1],
            rates=[0.9, 5.1],
        )


def test_convert_rate_info():
    rates = convert_operator_info([a, b, c])
    assert rates["46"] == {"name": "Operator_A", "rate": 0.17}
    assert rates["1"] == {"name": "Operator_C", "rate": 0.55}
    assert rates["48"] == {"name": "Operator_B", "rate": 1.2}


def test_compare_rates_from_operators():
    assert compare_rates_from_operators(op_rates, 460000000) == "Operator_A: 0.17"
    assert compare_rates_from_operators(op_rates, 987654321) == "Number is not callable"
    assert compare_rates_from_operators(op_rates, 467000000) == "Operator_B: 1.0"
    assert compare_rates_from_operators(op_rates, 467300000) == "Operator_A: 0.9"
    assert compare_rates_from_operators(op_rates, 467320000) == "Operator_A: 1.1"
    assert compare_rates_from_operators(op_rates, 100000000) == "Operator_C: 0.55"
