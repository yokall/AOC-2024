from pathlib import Path


def part1(lines: list[str]) -> int:
    list1 = []
    list2 = []

    for line in lines:
        int1, int2 = map(int, line.split())
        list1.append(int1)
        list2.append(int2)

    list1.sort()
    list2.sort()

    sum = 0
    for num1, num2 in zip(list1, list2):
        sum += abs(num1 - num2)

    return sum


def main():
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day01.txt"

    # Open the file
    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"part 1: {part1(lines)}")


if __name__ == "__main__":
    main()
