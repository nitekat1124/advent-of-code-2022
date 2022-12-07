from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        return self.find_marker(data, 4)

    def part2(self, data):
        return self.find_marker(data, 14)

    def find_marker(self, data, size):
        buffer = data[0]
        for i in range(size, len(buffer)):
            if len(set(buffer[:i][-size:])) == size:
                return i
