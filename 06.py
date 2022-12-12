from pathlib import Path

data_file = Path('data') / '06' / 'input.txt'

def find_stop_bitof_length(datafile: Path, length = 4) -> int:
    input_registers = [None] * length

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
                return i
                break
        else:
            raise Exception("Reached end without finding code")

print("Part 1", find_stop_bitof_length(data_file))
print("Part 2", find_stop_bitof_length(data_file, 14))

