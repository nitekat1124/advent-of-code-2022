from utils.solution_base import SolutionBase
from collections import deque
from math import prod


class Solution(SolutionBase):
    def part1(self, data):
        blueprints = self.parse_data(data)

        r = self.run_blueprints(blueprints, 24)
        return sum((i + 1) * v for i, v in enumerate(r))

    def part2(self, data):
        blueprints = self.parse_data(data)[:3]

        r = self.run_blueprints(blueprints, 32)
        return prod(r)

    def parse_data(self, data):
        blueprints = []
        for line in data:
            items = line.split()
            # blueprint present the formula of the minerals: (ore, clay, obsidian, geode)
            bp = [(int(items[6]), 0, 0, 0), (int(items[12]), 0, 0, 0), (int(items[18]), int(items[21]), 0, 0), (int(items[27]), 0, int(items[30]), 0)]
            blueprints.append(bp)

        return blueprints

    def run_blueprints(self, blueprints, time):
        r = []
        for bp in blueprints:
            # blueprint describe the costs for every robot: (ore, clay, obsidian, geode)

            # set the max reserves for each mineral to save some time
            max_reserves = [max(i) * 1.6 for i in zip(*bp)]
            max_reserves[3] = 99999

            # state = ((ore-robot, clay-robot, obsidian-robot, geode-robot), (ore, clay, obsidian, geode))
            state = ((1, 0, 0, 0), (0, 0, 0, 0))

            queue = deque([state])
            seen = set()
            remaining_time = time

            _max = 0
            while remaining_time > 0:
                for _ in range(len(queue)):

                    s = queue.popleft()
                    if s in seen:
                        continue

                    seen.add(s)
                    s1, s2 = s

                    # build geode robot
                    # if s2[0] >= bp[3][0] and s2[2] >= bp[3][2]:
                    if all(a >= b for a, b in zip(s2, bp[3])):
                        # s2n = tuple(a - b + c for a, b, c in zip(s2, bp[3], s1))
                        s2n = tuple(min(a - b + c, d) for a, b, c, d in zip(s2, bp[3], s1, max_reserves))
                        s1n = tuple(a + b for a, b in zip(s1, (0, 0, 0, 1)))
                        if remaining_time == 1:
                            _max = max(_max, s2n[3])
                        else:
                            queue.append((s1n, s2n))
                    else:
                        # build ore robot
                        # if s1[0] < max_reserves[0] and s2[0] >= bp[0][0]:
                        if s1[0] < max_reserves[0] and all(a >= b for a, b in zip(s2, bp[0])):
                            # s2n = tuple(a - b + c for a, b, c in zip(s2, bp[0], s1))
                            s2n = tuple(min(a - b + c, d) for a, b, c, d in zip(s2, bp[0], s1, max_reserves))
                            s1n = tuple(a + b for a, b in zip(s1, (1, 0, 0, 0)))
                            if remaining_time == 1:
                                _max = max(_max, s2n[3])
                            else:
                                queue.append((s1n, s2n))

                        # build clay robot
                        # if s1[1] < max_reserves[1] and s2[0] >= bp[1][0]:
                        if s1[1] < max_reserves[1] and all(a >= b for a, b in zip(s2, bp[1])):
                            # s2n = tuple(a - b + c for a, b, c in zip(s2, bp[1], s1))
                            s2n = tuple(min(a - b + c, d) for a, b, c, d in zip(s2, bp[1], s1, max_reserves))
                            s1n = tuple(a + b for a, b in zip(s1, (0, 1, 0, 0)))
                            if remaining_time == 1:
                                _max = max(_max, s2n[3])
                            else:
                                queue.append((s1n, s2n))

                        # build obsidian robot
                        # if s1[2] < max_reserves[2] and s2[0] >= bp[2][0] and s2[1] >= bp[2][1]:
                        if s1[2] < max_reserves[2] and all(a >= b for a, b in zip(s2, bp[2])):
                            # s2n = tuple(a - b + c for a, b, c in zip(s2, bp[2], s1))
                            s2n = tuple(min(a - b + c, d) for a, b, c, d in zip(s2, bp[2], s1, max_reserves))
                            s1n = tuple(a + b for a, b in zip(s1, (0, 0, 1, 0)))
                            if remaining_time == 1:
                                _max = max(_max, s2n[3])
                            else:
                                queue.append((s1n, s2n))

                        # s2n = tuple(a + c for a, c in zip(s2, s1))
                        s2n = tuple(min(a + c, d) for a, c, d in zip(s2, s1, max_reserves))
                        s1n = tuple(i for i in s1)
                        if remaining_time == 1:
                            _max = max(_max, s2n[3])
                        else:
                            queue.append((s1n, s2n))

                remaining_time -= 1
            r += [_max]
        return r
