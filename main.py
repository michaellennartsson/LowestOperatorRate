import sys

from price_comparator import (
    compare_rates_from_operators,
    convert_operator_info,
    Operator,
)

try:
    operators = [
        Operator(
            name="Operator_A",
            area_codes=[1, 268, 46, 4620, 468, 4631, 4673, 46732],
            rates=[0.9, 5.1, 0.17, 0, 0.15, 0.15, 0.9, 1.1],
        ),
        Operator(
            name="Operator_B",
            area_codes=[1, 44, 46, 467, 48],
            rates=[0.92, 0.5, 0.2, 1, 1.2],
        ),
    ]
except Exception as e:
    sys.exit(f"Error: '{e}'")

operator_rates = convert_operator_info(operators)

print("Welcome to rate comparator! Quit by typing 'exit'")
input_number = ""
while True:
    input_number = input("Please enter a phone number to find the cheapest rate!\n")
    if input_number == "exit":
        sys.exit()
    if not input_number.isdigit():
        print("Input contains not only numbers!")
        continue
    print(compare_rates_from_operators(operator_rates, input_number))
