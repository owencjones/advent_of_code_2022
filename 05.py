from pprint import pprint
from re import compile

from util.read_data import read_data

input = read_data("05/input.txt").split('\n\n')

stacks_str, instructions = (input[0], input[1])

def parse_stacks(stacks_str) -> list[list[str]]:
    stacks_str = stacks_str.replace('    ', '[-] ').replace(' ','').replace("[", "").replace("]","")
    stacks_lines = stacks_str.split('\n')
    stacks_lines.pop()
    stacks_lines = [list(s) for s in stacks_lines]
    stacks_lines.reverse()

    stack_width = len(stacks_lines[0])
    stack_height = len(stacks_lines)

    stacks = []

    # Pivot input
    for y in range(0, stack_width):
        new_stack = []
        for x in range(0, stack_height):
            value = stacks_lines[x][y]
            if value == '-':
                break
            new_stack.append(value)
        stacks.append(new_stack)

    return stacks

def parse_instructions(instructions) -> list[tuple[int,int,int]]:
    regex = compile("move (\d+) from (\d+) to (\d+)")

    return [(int(regex.match(s)[1]), int(regex.match(s)[2]) -1, int(regex.match(s)[3])-1) for s in instructions.split('\n')]


def get_result(stacks_str, instructions_str, stage_two=False) -> str:
    stacks=parse_stacks(stacks_str)
    instructions=parse_instructions(instructions_str)

    for instruction in instructions:
        amount, move_from, move_to = instruction
        print(f"moving {amount} blocks from stack {move_from+1} to {move_to+1}")

        blocks_moving=[]
        for _ in range(0, amount):
            blocks_moving.append(stacks[move_from].pop())
        
        if stage_two:
            blocks_moving.reverse()

        stacks[move_to] = [*stacks[move_to], *blocks_moving]
    
    final_state_code = [s[-1] for s in stacks]
    return "".join(final_state_code)


print(f"Part one {get_result(stacks_str, instructions)}, Part two: {get_result(stacks_str, instructions, True)}")    