from pathlib import Path
import pytest

from day07 import part1, part2, get_problem_parts, is_valid


def test_get_problem_parts() -> None:
    target, number_list = get_problem_parts("3267: 81 40 27")

    assert target == 3267
    assert number_list == [81, 40, 27]


@pytest.mark.parametrize(
    "target, number_list, expected, description",
    [
        (
            45,
            [45],
            True,
            "Should return True when a single number is in the number list and it matches the target number",
        ),
        (
            45,
            [2],
            False,
            "Should return False when a single number is in the number list and it matches the target number",
        ),
        (
            45,
            [40, 5],
            True,
            "Should return True when 2 numbers can be combined to make the target number by addition",
        ),
        (
            45,
            [9, 5],
            True,
            "Should return True when 2 numbers can be combined to make the target number by multiplication",
        ),
        (
            3267,
            [81, 40, 27],
            True,
            "Should return True when multiple numbers can be combined to make the target number by multiple operators",
        ),
        (
            7290,
            [6, 8, 6, 15],
            True,
            "Should return True when multiple numbers can be combined to make the target number by multiple operators including concatenation",
        ),
    ],
)
def test_is_valid(target, number_list, expected, description) -> None:
    result = is_valid(target, number_list)

    assert (
        result == expected
    ), f"Failed: {description}. Expected {expected}, but got {result}."


def test_part1() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day07.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    assert part1(lines) == 3749


def test_part2() -> None:
    script_dir = Path(__file__).parent

    # Specify the file path relative to the script directory
    file_path = script_dir / "data/day07.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    assert part2(lines) == 11387
