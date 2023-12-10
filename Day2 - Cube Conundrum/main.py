# Imports
from typing import List
# -------

# Common functions
# ----------------

# Part one
def part_one(input_array: List[str]) -> None:
    result = 0
    game_ids = []
    max_red = 12
    max_green = 13
    max_blue = 14

    for input_row in input_array:
        is_possible = True
        game_info = input_row.split(": ")[0]
        game_data = input_row.split(": ")[1]
        game_id = game_info.split(" ")[1]
        sets = game_data.split("; ")
        for set in sets:
            curr_cubes = {}
            curr_cubes["red"] = 0
            curr_cubes["green"] = 0
            curr_cubes["blue"] = 0
            cubes = set.split(", ")
            for cube in cubes:
                if "red" in cube:
                    curr_cubes["red"] = int(cube.split(" ")[0])
                elif "green" in cube:
                    curr_cubes["green"] = int(cube.split(" ")[0])
                elif "blue" in cube:
                    curr_cubes["blue"] = int(cube.split(" ")[0])
                if any([curr_cubes["red"] > max_red, curr_cubes["green"] > max_green, curr_cubes["blue"] > max_blue]):
                    is_possible = False
        if is_possible and game_id not in game_ids:
            game_ids.append(int(game_id))
    result = sum(game_ids)
    print(result)
# --------

# Part two
def part_two(input_array: List[str]) -> None:
    result = 0

    for input_row in input_array:
        pass
    print(result)
# --------

# Main wrapper
input_array = []
with open("Day2 - Cube Conundrum\input.txt", "r") as f:
    input_array = f.readlines()

part_one(input_array)
print("------------")
part_two(input_array)
# ------------