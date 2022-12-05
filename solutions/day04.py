from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        r = 0
        for line in data:
            s1, s2 = map(lambda section: tuple(map(int, section.split("-"))), line.split(","))
            # if s1[1] - s1[0] > s2[1] - s2[0]:
            #     s1, s2 = s2, s1
            # if s2[0] <= s1[0] and s1[1] <= s2[1]:
            #     r += 1
            if (s1[0] - s2[0]) * (s1[1] - s2[1]) <= 0:
                r += 1
        return r

    def part2(self, data):
        r = 0
        for line in data:
            s1, s2 = map(lambda section: tuple(map(int, section.split("-"))), line.split(","))
            # if s1[0] > s2[0]:
            #     s1, s2 = s2, s1
            # if s1[1] >= s2[0]:
            #     r += 1
            if s2[0] <= s1[0] <= s2[1] or s1[0] <= s2[0] <= s1[1]:
                r += 1
        return r
