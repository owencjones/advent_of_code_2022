from typing import Callable

from aoc.src import day_01

days = [day_01.do_output]

def wrap_day(day_number: int, output_function: Callable) -> None:
    print(f"Day 1: {day_number}")
    print(output_function())

[
    wrap_day(index, day_output_function)
    for index, day_output_function in enumerate(days)
]