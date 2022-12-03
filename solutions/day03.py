from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part{part_num}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part{part_num}")
        for i, r in zip(test_inputs, test_results):
            if len(r):
                if (tr := str(func(i))) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(f"your result: {tr}")
                    print(f"test answer: {r[0]}")
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

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
