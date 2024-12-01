import pytest

from pathlib import Path

from day01 import part1


def test_part1() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day01.txt"

    # Open the file
    with file_path.open("r") as file:
        lines = file.readlines()

    assert part1(lines) == 11
