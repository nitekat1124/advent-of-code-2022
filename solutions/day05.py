from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        self.check_is_raw()

        stacks = self.exec_procedures(data)
        return "".join(stacks[i][-1] for i in range(1, len(stacks)))

    def part2(self, data):
        self.check_is_raw()

        stacks = self.exec_procedures(data, multiple=True)
        return "".join(stacks[i][-1] for i in range(1, len(stacks)))

    def exec_procedures(self, data, multiple=False):
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
            moving_crates = stacks[_from][-move:]
            if not multiple:
                moving_crates = moving_crates[::-1]
            stacks[to].extend(moving_crates)
            # stacks[_from] = stacks[_from][:-move]
            del stacks[_from][-move:]

        return stacks
