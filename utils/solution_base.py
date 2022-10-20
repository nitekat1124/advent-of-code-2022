from utils.puzzle_reader import PuzzleReader


class SolutionBase:
    def __init__(self, day_num: int = -1, is_raw: bool = False):
        self.day_num = day_num
        self.is_raw = is_raw
        self.data = PuzzleReader.get_puzzle_input(self.day_num, self.is_raw)

    def get_test_input(self):
        return PuzzleReader.get_test_input(self.day_num, self.is_raw)

    def get_test_result(self, part_num):
        return PuzzleReader.get_test_result(self.day_num, part_num)
