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
        d += sum(2 * 5**i for i in range(math.ceil(math.log(d, 5))))
        r = []
        while d:
            d, n = divmod(d, 5)
            r += mapping[n - 2]
        return "".join(r[::-1])
