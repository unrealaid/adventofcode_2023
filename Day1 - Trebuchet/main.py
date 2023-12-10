# Imports
from typing import List

import re
# -------

# Common functions
# ----------------

# Part one
def part_one(input_array: List[str]) -> None:
    result = 0
    calibration_values = []

    for input_row in input_array:
        row_values = re.sub("\D+", "", input_row)
        if len(row_values) > 0:
            calibration_values.append(int("".join([row_values[0], row_values[-1]])))
    result = sum(calibration_values)
    print(result)
# --------

# Part two
def part_two(input_array: List[str]) -> None:
    result = 0
    calibration_values = []
    str_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        # "zero": "0",
    }

    def input_modifier(input_str):
        # ladder logic
        modified_input = []
        index = 0
        while index < len(input_str):
            if len(input_str) < 1:
                break
            if input_str[index].isnumeric():
                modified_input.append(input_str[index])
            elif any(input_str[index:].startswith(x) for x in ["o", "t", "f", "s", "e", "n"]):
                for key, value in str_digits.items():
                    if input_str[index:].startswith(key):
                        modified_input.append(value)
            index += 1
        return "".join(modified_input)

    for input_row in input_array:
        new_input = input_modifier(input_row.replace("\n", ""))
        row_values = re.sub("\D+", "", new_input)
        if len(row_values) > 0:
            calibration_values.append(int("".join([row_values[0], row_values[-1]])))
    result = sum(calibration_values)
    print(result)
# --------

# Main wrapper
input_array = []
with open("Day1 - Trebuchet\input.txt", "r") as f:
    input_array = f.readlines()

part_one(input_array)
print("------------")
part_two(input_array)
# ------------