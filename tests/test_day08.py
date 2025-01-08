from pathlib import Path

from day08 import part1, part2, get_points, get_distance_between_points


def test_get_points() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day08.txt"

    with file_path.open("r") as file:
        lines = [line.strip() for line in file.readlines()]

    expected = {
        "0": [(8, 1), (5, 2), (7, 3), (4, 4)],
        "A": [(6, 5), (8, 8), (9, 9)],
    }

    actual = get_points(lines)

    assert actual == expected


def test_get_distance_between_points() -> None:
    a = (6, 5)
    b = (8, 8)

    distance = get_distance_between_points(a, b)

    assert distance == (2, 3)


def test_part1() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day08.txt"

    with file_path.open("r") as file:
        lines = [line.strip() for line in file.readlines()]

    assert part1(lines) == 14


def test_part2() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day08.txt"

    with file_path.open("r") as file:
        lines = [line.strip() for line in file.readlines()]

    assert part2(lines) == 11387
