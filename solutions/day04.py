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
