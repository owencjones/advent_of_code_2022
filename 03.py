from typing import List, Tuple

from util.read_data import read_data


input = read_data("03/input.txt")

rucksacks = input.split('\n')

PRIORITY_MAP = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
get_priority = lambda s: PRIORITY_MAP.find(s) or None

halves = lambda lst: (
    lst[:len(lst)//2],
    lst[len(lst)//2:]
)

compartments = [halves(r) for r in rucksacks]

running_totals = []
for index, compartments in enumerate(compartments):
    compartment1, compartment2 = compartments
    op=set()
    priority = 0
    for char in compartment1:
        if char in compartment2:
            op.add(char)

    rucksack_total = sum([get_priority(i) for i in list(op)])
    running_totals.append(rucksack_total)

print(f"Running total added to: {sum(running_totals)}")

def group_in_lines_of_three(l: List[str]) -> List[Tuple[str,str,str]]:
    return [(l[i], l[i+1], l[i+2]) for i in range(0, len(l), 3)]

def whats_in_all_of_em(rucksack_group: Tuple[str, str, str]) -> str:
    rucksack1, rucksack2, rucksack3 = rucksack_group

    for char in rucksack1:
        if char in rucksack2 and char in rucksack3:
            return char


in_all_of_em = [
    whats_in_all_of_em(rucksack_group) 
    for rucksack_group in group_in_lines_of_three(rucksacks)
]

print(f"Total part two: {sum(list(map(get_priority,in_all_of_em)))}")