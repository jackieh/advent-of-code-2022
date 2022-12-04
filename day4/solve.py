from typing import List, Tuple


def parse_pair(pair: str) -> Tuple[int, int]:
    """
    Parse a pair of coordinates into a pair of integers.
    """
    split = pair.split('-')
    return int(split[0]), int(split[1])


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Parse a line of the input file into a pair of pairs.
    """
    split = line.split(',')
    return parse_pair(split[0]), parse_pair(split[1])


def get_pairs_of_pairs_from_file(file_path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Parse each line of the file into a pair of pairs.
    """
    with open(file_path) as f:
        lines = f.readlines()
    return [parse_line(line) for line in lines]


def contains(pair1: Tuple[int, int], pair2: Tuple[int, int]) -> bool:
    """
    Check if pair1 contains pair2.
    """
    return pair1[0] <= pair2[0] and pair1[1] >= pair2[1]


def overlaps(pair1: Tuple[int, int], pair2: Tuple[int, int]) -> bool:
    """
    Check if pair1 overlaps pair2.
    """
    return (
            contains(pair1, pair2)
            or contains(pair2, pair1)
            or pair1[0] <= pair2[0] <= pair1[1]
            or pair1[0] <= pair2[1] <= pair1[1]
    )


def part_1(file_path: str) -> str:
    """
    Parse each line of the file into a pair of pairs. On each line, identify
    if one pair contains the other pair. Count the number of lines where this
    is the case.
    """
    pairs_of_pairs = get_pairs_of_pairs_from_file(file_path)
    contained_pairs = [
        pairs for pairs in pairs_of_pairs if contains(pairs[0], pairs[1]) or contains(pairs[1], pairs[0])
    ]
    return str(len(contained_pairs))


def part_2(file_path: str) -> str:
    """
    Parse each line of the file into a pair of pairs. On each line, identify
    if one pair overlaps the other pair. Count the number of lines where this
    is the case.
    """
    pairs_of_pairs = get_pairs_of_pairs_from_file(file_path)
    overlapping_pairs = [
        pairs for pairs in pairs_of_pairs if overlaps(pairs[1], pairs[0])
    ]
    return str(len(overlapping_pairs))


def solve() -> None:
    print('Part 1 example:', part_1('day4/example.txt'))
    print('Part 1 input:', part_1('day4/input.txt'))
    print('Part 2 example:', part_2('day4/example.txt'))
    print('Part 2 input:', part_2('day4/input.txt'))
