from utils.solution_base import SolutionBase
from functools import cmp_to_key


class Solution(SolutionBase):
    def part1(self, data):
        data = [[*map(eval, i.split("\n"))] for i in "\n".join(data).split("\n\n")]
        return sum(idx + 1 for idx, [a, b] in enumerate(data) if self.compare(a, b) < 0)

    def part2(self, data):
        data = [*map(eval, [i for i in data if i != ""])] + [[[2]], [[6]]]
        data.sort(key=cmp_to_key(self.compare))
        return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)

    def compare(self, ax, bx):
        a = ax if type(ax) == int else [x for x in ax]
        b = bx if type(bx) == int else [x for x in bx]
        idx = 0

        res = {"right": -1, "wrong": 1}

        while 1:
            if idx == len(a):
                break

            if idx >= len(b):
                return res["wrong"]
            else:
                type_a = type(a[idx])
                type_b = type(b[idx])

                if type_a != type_b:
                    if type_a == int:
                        a[idx] = [a[idx]]
                        type_a = type(a[idx])
                    else:
                        b[idx] = [b[idx]]
                        type_b = type(b[idx])

                if type_a == int:
                    if a[idx] == b[idx]:
                        idx += 1
                        continue
                    else:
                        return res["right" if a[idx] < b[idx] else "wrong"]
                else:
                    x = self.compare(a[idx], b[idx])
                    if x in res.values():
                        return x
                    else:
                        idx += 1
                        continue

        return res["right"] if idx < len(b) else None
