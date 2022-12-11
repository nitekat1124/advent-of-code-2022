from utils.solution_base import SolutionBase
from collections import deque
from math import lcm


class Solution(SolutionBase):
    def part1(self, data):
        monkeys = self.parse_data(data)

        for _ in range(20):
            for m in monkeys:
                while m["items"]:
                    m["times"] += 1
                    worry = m["items"].popleft()
                    worry = m["ope"](worry)
                    worry //= 3
                    test = worry % m["test"] == 0
                    target = m["target"][test]
                    monkeys[target]["items"].append(worry)

        times = sorted(m["times"] for m in monkeys)
        return times[-1] * times[-2]

    def part2(self, data):
        monkeys = self.parse_data(data)
        test_lcm = lcm(*[i["test"] for i in monkeys])

        for _ in range(10000):
            for m in monkeys:
                while m["items"]:
                    m["times"] += 1
                    worry = m["items"].popleft()
                    worry = m["ope"](worry)
                    worry %= test_lcm
                    test = worry % m["test"] == 0
                    target = m["target"][test]
                    monkeys[target]["items"].append(worry)

        times = sorted(m["times"] for m in monkeys)
        return times[-1] * times[-2]

    def parse_data(self, data):
        data = [i.split("\n") for i in ("\n".join(data)).split("\n\n")]

        monkeys = []
        for i in data:
            items = deque([*map(int, i[1].split(":")[1].strip().split(", "))])
            ope = self.parse_operation(i[2].split("=")[1].strip())
            test = int(i[3].split("by")[1].strip())
            target = [int(i[5].split("monkey")[1].strip()), int(i[4].split("monkey")[1].strip())]  # [if_false, if_true]

            monkey = {"items": items, "ope": ope, "test": test, "target": target, "times": 0}
            monkeys.append(monkey)

        return monkeys

    def parse_operation(self, ope):
        match ope.split():
            case ["old", "+", "old"]:
                return lambda x: x + x
            case ["old", "+", val]:
                return lambda x: x + int(val)
            case ["old", "*", "old"]:
                return lambda x: x * x
            case ["old", "*", val]:
                return lambda x: x * int(val)
