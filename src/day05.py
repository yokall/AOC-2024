from pathlib import Path
import re


def part1(lines: list[str]) -> int:
    sum = 0

    rules, updates = getRulesAndUpdates(lines)

    goodUpdates, badUpdates = getGoodAndBadUpdates(rules, updates)

    for update in goodUpdates:
        middleIndex = int(len(update) / 2)

        sum += update[middleIndex]

    return sum


def part2(lines: list[str]) -> int:
    sum = 0

    rules, updates = getRulesAndUpdates(lines)

    goodUpdates, badUpdates = getGoodAndBadUpdates(rules, updates)

    for update in badUpdates:
        middleIndex = int(len(update) / 2)

        sum += update[middleIndex]

    return sum


def getRulesAndUpdates(lines: list[str]) -> list[list[int]]:
    rules = []
    updates = []

    rulePattern = r"(\d\d)\|(\d\d)"
    updatesPattern = r"^\d\d,"

    for line in lines:
        ruleMatch = re.match(rulePattern, line.strip())
        updatesMatch = re.match(updatesPattern, line.strip())

        if ruleMatch:
            rules.append([int(ruleMatch.group(1)), int(ruleMatch.group(2))])
        elif updatesMatch:
            updates.append(list(map(int, line.strip().split(","))))

    return rules, updates


def getGoodAndBadUpdates(rules: list[int], updates: list[int]) -> list[list[int]]:
    goodUpdates = []
    badUpdates = []

    for update in updates:
        goodUpdate = True
        for rule in rules:
            num1 = rule[0]
            num2 = rule[1]
            num1Index = update.index(num1) if num1 in update else -1
            num2Index = update.index(num2) if num2 in update else -1

            if num1Index != -1 and num2Index != -1 and num1Index > num2Index:
                goodUpdate = False

        if goodUpdate:
            goodUpdates.append(update)
        else:
            badUpdates.append(update)

    return goodUpdates, badUpdates


def main():
    script_dir = Path(__file__).parent

    file_path = script_dir / "data/day05.txt"

    with file_path.open("r") as file:
        lines = file.readlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
