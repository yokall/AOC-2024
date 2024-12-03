from pathlib import Path


def part1(reports: list[str]) -> int:
    safe_count = 0

    for report in reports:
        levels = list(map(int, report.split()))

        badIndex = checkForBadLevels(levels)

        if badIndex == -1:
            safe_count += 1

    return safe_count


def checkForBadLevels(levels: list[int]) -> int:
    current_direction = 0

    for index in range(1, len(levels) - 1):
        level = levels[index]

        next_level = levels[index + 1]
        difference = next_level - level

        if difference == 0:
            return index
        elif difference < 0:
            direction = 1
        else:
            direction = -1

        if current_direction == 0:
            current_direction = direction
        elif direction != current_direction:
            return index

        if abs(difference) > 3:
            return index

    return -1


# solution stolen from reddit https://www.reddit.com/r/adventofcode/comments/1h4ncyr/comment/m0041k3/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
def part2(reports: list[str]) -> int:
    reports = [[int(level) for level in report.split()] for report in reports]

    safe_count = sum(
        [
            any([is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))])
            for report in reports
        ]
    )

    return safe_count


def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


def main():
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day02.txt"

    # Open the file
    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
