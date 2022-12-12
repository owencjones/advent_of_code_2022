from pathlib import Path

data_file = Path('data') / '06' / 'input.txt'


input_registers = [None, None, None, None]

with data_file.open() as file:
    i = 0
    while True:
        char = file.read(1)

        i += 1

        input_registers.pop(0)
        input_registers.append(char)

        if any([i is None for i in input_registers]):
            continue

        if len(input_registers) == len(set(input_registers)):
            print(f"Stopped at file position {i}, with code {''.join(input_registers)}")
            break
    else:
        print("Reached end without finding code")

print('Done')

