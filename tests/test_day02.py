from pathlib import Path

from day02 import part1, part2


def test_part1() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day02.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    assert part1(lines) == 2


# def test_part2() -> None:
#     script_dir = Path(__file__).parent

#     # Specify the file path relative to the script directory
#     file_path = script_dir / "data/day01.txt"

#     # Open the file
#     with file_path.open("r") as file:
#         lines = file.readlines()

#     assert part2(lines) == 31
