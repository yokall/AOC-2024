from pathlib import Path


def get_problem_parts(problem: str) -> {int, list[int]}:
    first_part, second_part = problem.split(":")

    # Extract the first integer
    target = int(first_part.strip())

    # Extract the integers after the ':' into a list
    number_list = [int(num) for num in second_part.split()]

    return target, number_list


def is_valid(target: int, number_list: list[int], include_concat: bool) -> bool:
    if len(number_list) == 1:
        return target == number_list[0]

    first, second, *remaining = number_list

    if is_valid(target, [(first + second), *remaining], include_concat):
        return True

    if is_valid(target, [(first * second), *remaining], include_concat):
        return True

    if include_concat and is_valid(
        target, [(int(str(first) + str(second))), *remaining], include_concat
    ):
        return True

    return False


def part1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        target, number_list = get_problem_parts(line)

        if is_valid(target, number_list, False):
            sum += target

    return sum


def part2(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        target, number_list = get_problem_parts(line)

        if is_valid(target, number_list, True):
            sum += target

    return sum


def main():
    script_dir = Path(__file__).parent

    file_path = script_dir / "data/day07.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
