from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        priorities = 0
        for line in data:
            _sep = len(line) // 2
            items1, items2 = set(line[:_sep]), set(line[_sep:])
            badge = items1.intersection(items2).pop()
            priorities += ord(badge) - [38, 96][badge.islower()]
        return priorities

    def part2(self, data):
        priorities = 0
        for i in range(0, len(data), 3):
            rucksack1, rucksack2, rucksack3 = map(set, data[i : i + 3])
            badge = rucksack1.intersection(rucksack2, rucksack3).pop()
            priorities += ord(badge) - [38, 96][badge.islower()]
        return priorities
