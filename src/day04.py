from pathlib import Path


def part1(lines: list[str]) -> int:
    sum = 0

    grid = []

    for line in lines:
        grid.append(list(line))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]

            if char == "X":
                # to right
                if x <= len(grid[y]) - 4:
                    if (
                        grid[y][x + 1] == "M"
                        and grid[y][x + 2] == "A"
                        and grid[y][x + 3] == "S"
                    ):
                        sum += 1
                # to left
                if x >= 3:
                    if (
                        grid[y][x - 1] == "M"
                        and grid[y][x - 2] == "A"
                        and grid[y][x - 3] == "S"
                    ):
                        sum += 1
                # down
                if y <= len(grid) - 4:
                    if (
                        grid[y + 1][x] == "M"
                        and grid[y + 2][x] == "A"
                        and grid[y + 3][x] == "S"
                    ):
                        sum += 1
                # up
                if y >= 3:
                    if (
                        grid[y - 1][x] == "M"
                        and grid[y - 2][x] == "A"
                        and grid[y - 3][x] == "S"
                    ):
                        sum += 1
                # up and to left
                if x >= 3 and y >= 3:
                    if (
                        grid[y - 1][x - 1] == "M"
                        and grid[y - 2][x - 2] == "A"
                        and grid[y - 3][x - 3] == "S"
                    ):
                        sum += 1
                # up and to right
                if x <= len(grid[y]) - 4 and y >= 3:
                    if (
                        grid[y - 1][x + 1] == "M"
                        and grid[y - 2][x + 2] == "A"
                        and grid[y - 3][x + 3] == "S"
                    ):
                        sum += 1
                # down and to left
                if x >= 3 and y <= len(grid) - 4:
                    if (
                        grid[y + 1][x - 1] == "M"
                        and grid[y + 2][x - 2] == "A"
                        and grid[y + 3][x - 3] == "S"
                    ):
                        sum += 1
                # down and to right
                if x <= len(grid[y]) - 4 and y <= len(grid) - 4:
                    if (
                        grid[y + 1][x + 1] == "M"
                        and grid[y + 2][x + 2] == "A"
                        and grid[y + 3][x + 3] == "S"
                    ):
                        sum += 1

    return sum


def part2(lines: list[str]) -> int:
    sum = 0

    grid = []

    for line in lines:
        grid.append(list(line.strip()))

    rowCount = len(grid)
    for y in range(len(grid)):
        if y < 1 or y > rowCount - 2:
            continue

        rowLength = len(grid[y])

        for x in range(len(grid[y])):
            if x < 1 or x >= rowLength - 1:
                continue

            char = grid[y][x]

            if char == "A":
                topLeft = grid[y - 1][x - 1]
                topRight = grid[y - 1][x + 1]
                bottomLeft = grid[y + 1][x - 1]
                bottomRight = grid[y + 1][x + 1]

                if (
                    (topLeft == "M" and bottomRight == "S")
                    or (topLeft == "S" and bottomRight == "M")
                ) and (
                    (topRight == "M" and bottomLeft == "S")
                    or (topRight == "S" and bottomLeft == "M")
                ):
                    sum += 1

    return sum


def main():
    script_dir = Path(__file__).parent

    file_path = script_dir / "data/day04.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
