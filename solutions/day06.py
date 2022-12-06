from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        buffer = data[0]
        for i in range(4, len(buffer)):
            if len(set(buffer[:i][-4:])) == 4:
                return i

    def part2(self, data):
        buffer = data[0]
        for i in range(14, len(buffer)):
            if len(set(buffer[:i][-14:])) == 14:
                return i
