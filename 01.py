from util import read_data
from typing import Tuple, List


input = read_data("01/input.txt")

elves: List[int] = sorted(
    [
        sum(elf)
        for elf in [list(map(int, elf)) for elf in [elf.split('\n') for elf in input.split("\n\n")]]
    ]
)

def output(elves) -> Tuple[int, int]:
    return (
        elves[-1],
        sum(elves[-3:])
    )

def do_output() -> None:
    output_answers = output(elves)
    print(f"The max elf is {output_answers[0]}, and the top three add up to {output_answers[1]}")

if __name__ == "__main__":
    do_output()
