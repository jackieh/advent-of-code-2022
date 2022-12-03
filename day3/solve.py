from typing import List, Tuple


def letter_to_number(letter: str) -> int:
    """
    a through z are 1 through 26. A through Z are 27 through 52.
    """
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def part_1(file_path: str) -> str:
    # Read the file into a list of strings
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    # Split each line in half into a pair, resulting in a list of tuples
    pairs = [(line[:len(line)//2], line[len(line)//2:]) for line in lines]

    # For each pair, find the letter that is the same in both halves
    def find_common_letters(pair: Tuple[str, str]) -> str:
        # For each letter in the first half, check if it's in the second half
        for letter in pair[0]:
            if letter in pair[1]:
                return letter
    common_letters = [find_common_letters(pair) for pair in pairs]

    # Map each letter to its corresponding number
    priorities = [letter_to_number(letter) for letter in common_letters]
    # Add the numbers together
    result = sum(priorities)
    return str(result)


def part_2(file_path: str) -> str:
    # Read the file into a list of lists of three lines
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    # Split the list into a list of lists of three lines
    groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

    # For each group, find the letter that is the same in all three lines
    def find_common_letters(group: List[str]) -> str:
        # For each letter in the first line, check if it's in the other two lines
        for letter in group[0]:
            if letter in group[1] and letter in group[2]:
                return letter
    common_letters = [find_common_letters(group) for group in groups]

    # Map each letter to its corresponding number
    priorities = [letter_to_number(letter) for letter in common_letters]
    # Add the numbers together
    result = sum(priorities)
    return str(result)


def solve() -> None:
    print('Part 1 example:', part_1('day3/example.txt'))
    print('Part 1 input:', part_1('day3/input.txt'))
    print('Part 2 example:', part_2('day3/example.txt'))
    print('Part 2 input:', part_2('day3/input.txt'))
