from typing import List, Tuple


symbols1 = {
    'A': 1,
    'B': 2,
    'C': 3,
}


symbols2 = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


game_results_from_moves = {
    (1, 1): 3,  # Rock rock
    (1, 2): 6,  # Rock paper
    (1, 3): 0,  # Rock scissors
    (2, 1): 0,  # Paper rock
    (2, 2): 3,  # Paper paper
    (2, 3): 6,  # Paper scissors
    (3, 1): 6,  # Scissors rock
    (3, 2): 0,  # Scissors paper
    (3, 3): 3,  # Scissors scissors
}


def get_parsed_lines_from_text_input(file_path: str) -> List[List[int]]:
    # Read lines from input file
    with open(file_path) as f:
        lines = f.read().splitlines()
    # Split string by whitespace on each line
    parsed_lines = [line.split() for line in lines]
    # Convert each string to int from the symbols1 and symbols2 dicts
    return [[symbols1[char] for char in line[0]] + [symbols2[char] for char in line[1]] for line in parsed_lines]


def part_1(file_path: str) -> str:
    lines = get_parsed_lines_from_text_input(file_path)
    # Add up the scores for each line
    score = 0
    for line in lines:
        score += game_results_from_moves[(line[0], line[1])] + line[1]
    return str(score)


def part_2(file_path: str) -> str:
    def get_move_2(move_1: int, game_outcome: int) -> Tuple[int, int]:
        target_win_score = (game_outcome - 1) * 3
        for test_move in [1, 2, 3]:
            if target_win_score == game_results_from_moves[(move_1, test_move)]:
                return test_move, target_win_score
    lines = get_parsed_lines_from_text_input(file_path)
    # Add up the scores for each line
    score = 0
    for line in lines:
        move_2, win_score = get_move_2(line[0], line[1])
        score += move_2 + win_score
    return str(score)


def solve() -> None:
    print('Part 1 example:', part_1('day2/example.txt'))
    print('Part 1 input:', part_1('day2/input.txt'))
    print('Part 2 example:', part_2('day2/example.txt'))
    print('Part 2 input:', part_2('day2/input.txt'))
