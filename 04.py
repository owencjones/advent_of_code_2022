from util.read_data import read_data

input = read_data("04/input.txt")
ranges = [list(j.split('-') for j in i) for i in [i.split(',') for i in input.split('\n')]]

count_part_one = 0
count_part_two = 0

for range_factors in ranges:
    range_a = range(int(range_factors[0][0]), int(range_factors[0][1]) + 1)
    range_b = range(int(range_factors[1][0]), int(range_factors[1][1]) + 1)

    contains = lambda a,b: (a.start <= b.start) and (a.stop >= b.stop)
    contains_either = lambda a, b: contains(a,b) or contains(b,a)
    add = contains_either(range_a, range_b)

    count_part_one += 1 if add else 0

    def overlaps(a, b) -> bool:
        list_a = list(a)
        list_b = list(b)

        for i in list_a:
            if i in list_b:
                return True
        
        return False

    count_part_two += 1 if overlaps(range_a, range_b) else 0

print("Part one", count_part_one)
print("Part two", count_part_two)
