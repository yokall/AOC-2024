from pathlib import Path
import re


def part1(lines: list[str]) -> int:
    mulPattern = r"mul\(\d{1,3},\d{1,3}\)"
    numberPattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    sum = 0

    for line in lines:
        for mul in re.finditer(mulPattern, line):
            match = re.match(numberPattern, mul.group())

            if match:
                # Extract the integers as strings and convert them to integers
                num1, num2 = int(match.group(1)), int(match.group(2))

                sum += num1 * num2

    return sum


def part2(lines: list[str]) -> int:
    mulPattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    numberPattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    dontPattern = r"don't\(\)"
    doPattern = r"do\(\)"

    sum = 0
    enabled = True

    for line in lines:
        for mul in re.finditer(mulPattern, line):
            match = re.match(numberPattern, mul.group())

            if match and enabled:
                # Extract the integers as strings and convert them to integers
                num1, num2 = int(match.group(1)), int(match.group(2))

                sum += num1 * num2

            match = re.match(dontPattern, mul.group())

            if match:
                enabled = False

            match = re.match(doPattern, mul.group())

            if match:
                enabled = True

    return sum


def main():
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day03.txt"

    # Open the file
    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
