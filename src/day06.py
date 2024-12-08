from enum import Enum
from pathlib import Path


class Direction(Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class Guard:
    def __init__(self, position, direction, out_of_bounds):
        self.position = position
        self.direction = direction  # Direction Enum
        self.out_of_bounds = out_of_bounds

    def __repr__(self):
        return f"Guard(position={self.position}, direction={self.direction.value}, out_of_bounds={self.out_of_bounds})"


def part1(lines: list[str]) -> int:
    obstacles = set()

    guard = Guard(position=(-1, -1), direction=Direction.NORTH, out_of_bounds=False)
    path = set()
    height = len(lines)
    width = len(lines[0])

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                guard.position = (x, y)

    while not guard.out_of_bounds:
        updateGuardPosition(guard, obstacles, width, height, path)

    return len(path)


def updateGuardPosition(
    guard: Guard, obstacles: set[tuple], width: int, height: int, path: set[tuple]
) -> None:
    if guard.direction == Direction.NORTH:
        obstaclesInPath = [
            (x, y)
            for x, y in obstacles
            if x == guard.position[0] and y < guard.position[1]
        ]

        if obstaclesInPath:
            obstaclesInPath.sort(key=lambda coord: coord[1], reverse=True)
            obstacle = obstaclesInPath[0]

            for y in range(guard.position[1] - 1, obstacle[1] + 1, -1):
                path.add((guard.position[0], y))

            guard.position = (guard.position[0], obstacle[1] + 1)
            guard.direction = Direction.EAST
        else:
            for y in range(guard.position[1] - 1, 0, -1):
                path.add((guard.position[0], y))
            guard.out_of_bounds = True
    elif guard.direction == Direction.EAST:
        obstaclesInPath = [
            (x, y)
            for x, y in obstacles
            if x > guard.position[0] and y == guard.position[1]
        ]

        if obstaclesInPath:
            obstaclesInPath.sort(key=lambda coord: coord[1])
            obstacle = obstaclesInPath[0]

            for x in range(guard.position[0] + 1, obstacle[0] - 1):
                path.add((x, guard.position[1]))

            guard.position = (obstacle[0] - 1, guard.position[1])
            guard.direction = Direction.SOUTH
        else:
            for x in range(guard.position[0] + 1, (width - 1)):
                path.add((x, guard.position[1]))
            guard.out_of_bounds = True
    elif guard.direction == Direction.SOUTH:
        obstaclesInPath = [
            (x, y)
            for x, y in obstacles
            if x == guard.position[0] and y > guard.position[1]
        ]

        if obstaclesInPath:
            obstaclesInPath.sort(key=lambda coord: coord[1])
            obstacle = obstaclesInPath[0]

            for y in range(guard.position[1] + 1, obstacle[1] - 1):
                path.add((guard.position[0], y))

            guard.position = (guard.position[0], obstacle[1] - 1)
            guard.direction = Direction.WEST
        else:
            for y in range(guard.position[1] + 1, (height - 1)):
                path.add((guard.position[0], y))
            guard.out_of_bounds = True
    elif guard.direction == Direction.WEST:
        obstaclesInPath = [
            (x, y)
            for x, y in obstacles
            if x < guard.position[0] and y == guard.position[1]
        ]

        if obstaclesInPath:
            obstaclesInPath.sort(key=lambda coord: coord[1], reverse=True)
            obstacle = obstaclesInPath[0]

            for x in range(guard.position[0] - 1, obstacle[0] + 1, -1):
                path.add((x, guard.position[1]))

            guard.position = (obstacle[0] + 1, guard.position[1])
            guard.direction = Direction.NORTH
        else:
            for x in range(guard.position[0] - 1, 0, -1):
                path.add((x, guard.position[1]))
            guard.out_of_bounds = True


def part2(lines: list[str]) -> int:
    return 1


def main():
    script_dir = Path(__file__).parent

    file_path = script_dir / "data/day06.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
