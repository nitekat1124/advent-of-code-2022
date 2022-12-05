from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        items = [sum(map(int, elf.split("\n"))) for elf in "\n".join(data).split("\n\n")]
        return max(items)

    def part2(self, data):
        items = [sum(map(int, elf.split("\n"))) for elf in "\n".join(data).split("\n\n")]
        return sum(sorted(items)[-3:])
