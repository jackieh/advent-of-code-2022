from typing import List


def get_sums_of_elements_from_text_input(file_path: str) -> List[int]:
    # Read groups of lines from input file
    with open(file_path) as f:
        groups = [group.splitlines() for group in f.read().split('\n\n')]
    # Parse all the list elements from strings to ints
    groups = [[int(x) for x in group] for group in groups]
    # Sum the elements of each list
    return [sum(group) for group in groups]


def part_1(file_path: str) -> str:
    sums = get_sums_of_elements_from_text_input(file_path)
    # Print the max element in the list
    return str(max(sums))


def part_2(file_path: str) -> str:
    sums = get_sums_of_elements_from_text_input(file_path)
    # Print the sum of the max three elements in the list
    return str(sum(sorted(sums)[-3:]))


def solve() -> None:
    print('Part 1 example:', part_1('day1/example.txt'))
    print('Part 1 input:', part_1('day1/input.txt'))
    print('Part 2 example:', part_2('day1/example.txt'))
    print('Part 2 input:', part_2('day1/input.txt'))
