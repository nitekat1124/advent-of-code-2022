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

    def check_is_raw(self):
        if self.is_raw is False:
            print("please use --raw flag in this puzzle")
            exit()

    def part1(self, data):
        self.check_is_raw()

        sep = [i for i, v in enumerate(data) if v == ""][0]

        crates = data[: sep - 1][::-1]
        procedures = data[sep + 1 :]

        stack_num = max(map(int, data[sep - 1].split()))
        stacks = [[] for _ in range(stack_num + 1)]

        for line in crates:
            items = [line[i] for i in range(1, len(line), 4)]
            for i, v in enumerate(items):
                if v != " ":
                    stacks[i + 1].append(v)

        for line in procedures:
            _, move, _, _from, _, to = [int(v) if i % 2 else v for i, v in enumerate(line.split())]
            stacks[to].extend(stacks[_from][-move:][::-1])
            # stacks[_from] = stacks[_from][:-move]
            del stacks[_from][-move:]

        return "".join(stacks[i][-1] for i in range(1, stack_num + 1))

    def part2(self, data):
        self.check_is_raw()

        sep = [i for i, v in enumerate(data) if v == ""][0]

        crates = data[: sep - 1][::-1]
        procedures = data[sep + 1 :]

        stack_num = max(map(int, data[sep - 1].split()))
        stacks = [[] for _ in range(stack_num + 1)]

        for line in crates:
            items = [line[i] for i in range(1, len(line), 4)]
            for i, v in enumerate(items):
                if v != " ":
                    stacks[i + 1].append(v)

        for line in procedures:
            _, move, _, _from, _, to = [int(v) if i % 2 else v for i, v in enumerate(line.split())]
            stacks[to].extend(stacks[_from][-move:])
            # stacks[_from] = stacks[_from][:-move]
            del stacks[_from][-move:]

        return "".join(stacks[i][-1] for i in range(1, stack_num + 1))
