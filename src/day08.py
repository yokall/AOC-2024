from pathlib import Path
from typing import Dict, List, Tuple


def get_points(lines: list[str]) -> Dict[str, List[Tuple[int, int]]]:
    points = {}
    for y, line in enumerate(lines):
        for x, point in enumerate(list(line.strip())):
            if point.isalnum():
                points.setdefault(point, []).append((x, y))

    return points


def get_distance_between_points(
    a: Tuple[int, int], b: Tuple[int, int]
) -> Tuple[int, int]:
    x_diff = b[0] - a[0]
    y_diff = b[1] - a[1]

    return (x_diff, y_diff)


def part1(lines: list[str]) -> int:
    antenna_groups = get_points(lines)

    antinodes = set()
    for frequency in antenna_groups:
        for antenna in antenna_groups[frequency]:
            for other_antenna in antenna_groups[frequency]:
                if other_antenna != antenna:
                    distance = get_distance_between_points(antenna, other_antenna)

                    antinode_x = antenna[0] + (distance[0] * -1)
                    antinode_y = antenna[1] + (distance[1] * -1)

                    if (
                        antinode_x >= 0
                        and antinode_y >= 0
                        and antinode_x < len(lines[0])
                        and antinode_y < len(lines)
                    ):
                        antinodes.add((antinode_x, antinode_y))

    return len(antinodes)


def part2(lines: list[str]) -> int:
    return 0


def main():
    script_dir = Path(__file__).parent

    file_path = script_dir / "data/day07.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
