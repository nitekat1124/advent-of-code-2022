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
        col1 = {"A": 1, "B": 2, "C": 3}
        col2 = {"X": 1, "Y": 2, "Z": 3}
        scores = {"L": 0, "D": 3, "W": 6}

        total_score = 0

        for line in data:
            shape1, shape2 = line.split()
            x = col1[shape1]
            y = col2[shape2]

            match y - x:
                case 0:
                    round = "D"
                case -2 | 1:
                    round = "W"
                case -1 | 2:
                    round = "L"

            total_score += y + scores[round]

        return total_score

    def part2(self, data):
        col1 = {"A": 1, "B": 2, "C": 3}
        col2 = {"X": 0, "Y": 3, "Z": 6}

        total_score = 0

        for line in data:
            shape1, shape2 = line.split()
            x = col1[shape1]
            round_score = col2[shape2]

            match round_score:
                case 6:  # win
                    y = x % 3 + 1
                case 3:  # draw
                    y = x
                case 0:  # loss
                    y = (x + 1) % 3 + 1

            total_score += y + round_score

        return total_score
