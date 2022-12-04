from util.read_data import read_data


input = read_data("01/input.txt")

elves = sorted(
    [
        sum(elf)
        for elf in [list(map(int, elf)) for elf in [elf.split('\n') for elf in input.split("\n\n")]]
    ]
)


print(f"The max elf is {elves[-1]}, and the top three add up to {sum(elves[-3:])}")
