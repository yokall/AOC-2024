from day03 import part1, part2


def test_part1() -> None:
    lines = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]

    assert part1(lines) == 161


def test_part2() -> None:
    lines = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]

    assert part2(lines) == 48
