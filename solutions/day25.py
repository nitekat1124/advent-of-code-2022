from utils.solution_base import SolutionBase
import math


class Solution(SolutionBase):
    def part1(self, data):
        return self.d2s(sum(self.s2d(i) for i in data))

    def part2(self, data):
        return "Merry Christmas!"

    def s2d(self, s):
        # return sum(("=-012".index(c) - 2) * 5**i for i, c in enumerate(s[::-1]))
        mapping = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
        return sum(mapping[c] * 5**i for i, c in enumerate(s[::-1]))

    def d2s(self, d):
        mapping = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
        exp = math.ceil(math.log(d, 5))
        d += sum(2 * 5**i for i in range(exp))
        return "".join(mapping[d // (5**i) % 5 - 2] for i in range(exp - 1, -1, -1))
