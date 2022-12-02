import day1
import day2


def print_solution_header(day_number):
    print('')
    print(f'--- Day {day_number} ---')
    print('')


def main():
    print_solution_header(1)
    day1.solve()
    print_solution_header(2)
    day2.solve()


if __name__ == '__main__':
    main()
