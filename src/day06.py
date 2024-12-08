from enum import Enum
from pathlib import Path
import copy


class Direction(Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class Guard:
    def __init__(self, map):
        self.map = map

        self.direction = Direction.NORTH
        self.position = self.get_start_position()

    def __repr__(self):
        return f"Guard(position={self.position}, direction={self.direction.value}, out_of_bounds={self.out_of_bounds})"

    @property
    def out_of_bounds(self):
        return (
            self.position[0] == 0
            or self.position[1] == 0
            or self.position[0] == len(self.map[0]) - 1
            or self.position[1] == len(self.map) - 1
        )

    def get_start_position(self):
        for r, row in enumerate(self.map):
            for c, char in enumerate(row):
                if char == "^":
                    return (c, r)


def part1(lines: list[str]) -> int:
    map = get_map(lines)

    guard = Guard(map=map)
    path = set()

    while not guard.out_of_bounds:
        path.add(guard.position)
        updateGuardPosition(guard, map)

    path.add(guard.position)

    return len(path)


def updateGuardPosition(guard: Guard, map: list[list[str]]) -> None:
    if guard.direction == Direction.NORTH:
        next_x = guard.position[0]
        next_y = guard.position[1] - 1
        next_square = map[next_y][next_x]

        if next_square == "#":
            guard.direction = Direction.EAST
        else:
            guard.position = (next_x, next_y)
    elif guard.direction == Direction.EAST:
        next_x = guard.position[0] + 1
        next_y = guard.position[1]
        next_square = map[next_y][next_x]

        if next_square == "#":
            guard.direction = Direction.SOUTH
        else:
            guard.position = (next_x, next_y)
    elif guard.direction == Direction.SOUTH:
        next_x = guard.position[0]
        next_y = guard.position[1] + 1
        next_square = map[next_y][next_x]

        if next_square == "#":
            guard.direction = Direction.WEST
        else:
            guard.position = (next_x, next_y)
    elif guard.direction == Direction.WEST:
        next_x = guard.position[0] - 1
        next_y = guard.position[1]
        next_square = map[next_y][next_x]

        if next_square == "#":
            guard.direction = Direction.NORTH
        else:
            guard.position = (next_x, next_y)


def part2(lines: list[str]) -> int:
    map = get_map(lines)

    guard = Guard(map=map)
    guard_start_position = guard.position
    original_path = set()

    while not guard.out_of_bounds:
        original_path.add(guard.position)
        updateGuardPosition(guard, map)

    original_path.add(guard.position)

    loop_count = 0

    for position in original_path:
        if position == guard_start_position:
            continue

        new_map = copy.deepcopy(map)
        new_map[position[1]][position[0]] = "#"

        new_guard = Guard(new_map)
        new_path = set()

        while not new_guard.out_of_bounds:
            point = {new_guard.position, new_guard.direction}

            if point in new_path:
                loop_count += 1
                break

            new_path.add(frozenset(point))
            updateGuardPosition(new_guard, new_map)

    return loop_count


def get_map(lines: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in lines]


def main():
    script_dir = Path(__file__).parent

    file_path = script_dir / "data/day06.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
