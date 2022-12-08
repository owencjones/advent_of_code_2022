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
    print(f"Rucksack {index}: Characters: {str(op)}, total {priority}")
    running_totals.append(rucksack_total)

print(f"Running total added to: {sum(running_totals)}")