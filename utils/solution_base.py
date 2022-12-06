from utils.puzzle_reader import PuzzleReader


class SolutionBase:
    def __init__(self, day_num: int = -1, is_raw: bool = False, skip_test: bool = False):
        self.day_num = day_num
        self.is_raw = is_raw
        self.skip_test = skip_test
        self.data = PuzzleReader.get_puzzle_input(self.day_num, self.is_raw)

    def get_test_input(self):
        return PuzzleReader.get_test_input(self.day_num, self.is_raw)

    def get_test_result(self, part_num):
        return PuzzleReader.get_test_result(self.day_num, part_num)

    def solve(self, part_num: int):
        if not self.skip_test:
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

    def check_is_raw(self):
        if self.is_raw is False:
            print("please use --raw flag in this puzzle")
            exit()
