from pathlib import Path


def part1(reports: list[str]) -> int:
    safe_count = 0

    for report in reports:
        levels = list(map(int, report.split()))

        current_direction = 0

        safe = 1

        for index, level in enumerate(levels):
            # Skip the first level as we are always comparing with the previous level
            if index == 0:
                continue

            previous_level = levels[index - 1]
            difference = previous_level - level

            if difference == 0:
                safe = 0
                break
            elif difference < 0:
                direction = 1
            else:
                direction = -1

            if current_direction == 0:
                current_direction = direction
            elif direction != current_direction:
                safe = 0
                break

            if abs(difference) > 3:
                safe = 0
                break

        safe_count += safe

    return safe_count


def part2(lines: list[str]) -> int:
    list1 = []
    list2 = []

    for line in lines:
        int1, int2 = map(int, line.split())
        list1.append(int1)
        list2.append(int2)

    sum = 0
    for num in list1:
        sum += num * list2.count(num)

    return sum


def main():
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day02.txt"

    # Open the file
    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
