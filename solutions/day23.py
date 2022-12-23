from collections import defaultdict
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        order = ["N", "S", "W", "E"]
        elves = self.parse_data(data)

        for _ in range(10):
            locations = defaultdict(int)
            elves_new = {}
            items = list(elves.items())
            for pos, v in items:
                if v == 0:
                    continue

                checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
                if all([elves[c] == 0 for c in checks]):
                    continue

                for d in order:
                    if d == "N":
                        checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1)]
                        new_pos = (pos[0] - 1, pos[1])
                    elif d == "S":
                        checks = [(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)]
                        new_pos = (pos[0] + 1, pos[1])
                    elif d == "W":
                        checks = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
                        new_pos = (pos[0], pos[1] - 1)
                    elif d == "E":
                        checks = [(pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
                        new_pos = (pos[0], pos[1] + 1)

                    if all([elves[c] == 0 for c in checks]):
                        elves_new[pos] = new_pos
                        locations[new_pos] += 1
                        break

            repeated = [p for p, c in locations.items() if c > 1]
            for pos_org, pos_new in elves_new.items():
                if pos_new not in repeated:
                    elves[pos_org] = 0
                    elves[pos_new] = 1

            order = order[1:] + [order[0]]

        p = [pos for pos, v in elves.items() if v == 1]
        min_x, max_x, min_y, max_y = self.get_region_corners(p)

        return (max_x - min_x + 1) * (max_y - min_y + 1) - len(p)

    def part2(self, data):
        order = ["N", "S", "W", "E"]
        elves = self.parse_data(data)

        state = self.gen_state(elves)
        round = 1

        while 1:
            locations = defaultdict(int)
            elves_new = {}
            items = list(elves.items())
            for pos, v in items:
                if v == 0:
                    continue

                checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
                if all([elves[c] == 0 for c in checks]):
                    continue

                for d in order:
                    if d == "N":
                        checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1)]
                        new_pos = (pos[0] - 1, pos[1])
                    elif d == "S":
                        checks = [(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)]
                        new_pos = (pos[0] + 1, pos[1])
                    elif d == "W":
                        checks = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
                        new_pos = (pos[0], pos[1] - 1)
                    elif d == "E":
                        checks = [(pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
                        new_pos = (pos[0], pos[1] + 1)

                    if all([elves[c] == 0 for c in checks]):
                        elves_new[pos] = new_pos
                        locations[new_pos] += 1
                        break

            repeated = [p for p, c in locations.items() if c > 1]
            for pos_org, pos_new in elves_new.items():
                if pos_new not in repeated:
                    elves[pos_org] = 0
                    elves[pos_new] = 1

            order = order[1:] + [order[0]]

            state_new = self.gen_state(elves)
            if state == (state & state_new):
                return round
            else:
                state = state_new

            round += 1

    def parse_data(self, data):
        elves = defaultdict(int)
        for i, line in enumerate(data):
            for j, c in enumerate(line):
                if c == "#":
                    elves[(i, j)] = 1
        return elves

    def get_region_corners(self, elves):
        min_x = float("inf")
        max_x = -float("inf")
        min_y = float("inf")
        max_y = -float("inf")

        for y, x in elves:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

        return min_x, max_x, min_y, max_y

    def gen_state(self, elves):
        return set(pos for pos, v in elves.items() if v == 1)
