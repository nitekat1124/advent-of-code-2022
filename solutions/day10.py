from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        x = 1
        cycle = 0

        signal_strengths_sum = 0
        checkpoints = [20, 60, 100, 140, 180, 220]

        for inst in data:
            if inst == "noop":
                v = 0
                cycles_to_take = 1
            else:
                _, v = inst.split()
                v = int(v)
                cycles_to_take = 2

            for c in checkpoints:
                if cycle < c <= cycle + cycles_to_take:
                    signal_strengths_sum += x * c
                    break

            cycle += cycles_to_take
            x += v
        return signal_strengths_sum

    def part2(self, data):
        x = 1
        cycle = 0

        crt = list("." * 240)
        sprite_pos = [i for i in [x - 1, x, x + 1] if i >= 0]

        for inst in data:
            if inst == "noop":
                v = 0
                cycles_to_take = 1
            else:
                _, v = inst.split()
                v = int(v)
                cycles_to_take = 2

            for i in range(cycles_to_take):
                pos = cycle + i
                if pos % 40 in sprite_pos:
                    crt[pos] = "#"

            cycle += cycles_to_take
            x += v
            sprite_pos = [i for i in [x - 1, x, x + 1] if i >= 0]

        for i in range(0, 240, 40):
            print("".join(crt[i : i + 40]))
        print()

        return "".join(crt)
