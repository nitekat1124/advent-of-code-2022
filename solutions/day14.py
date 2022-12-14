from utils.solution_base import SolutionBase
from collections import defaultdict

"""
0: air (.)
1: rock (#)
2: sand (+)
3: rested sand (o)
"""


class Solution(SolutionBase):
    def part1(self, data):
        sand = (500, 0)

        _map = defaultdict(int)
        _map[sand] = 2

        for line in data:
            coords = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
            for i in range(len(coords) - 1):
                if coords[i][0] == coords[i + 1][0]:
                    a, b = coords[i][1], coords[i + 1][1]
                    if a > b:
                        a, b = b, a
                    for j in range(a, b + 1):
                        _map[(coords[i][0], j)] = 1
                else:
                    a, b = coords[i][0], coords[i + 1][0]
                    if a > b:
                        a, b = b, a
                    for j in range(a, b + 1):
                        _map[(j, coords[i][1])] = 1

        max_y = max([i[1] for i in _map.keys()])

        while sand[1] < max_y:
            next_sands = [(sand[0], sand[1] + 1), (sand[0] - 1, sand[1] + 1), (sand[0] + 1, sand[1] + 1)]
            for next_sand in next_sands:
                if _map[next_sand] == 0:
                    _map[sand] = 0
                    _map[next_sand] = 2
                    sand = next_sand
                    break
            else:
                _map[sand] = 3
                sand = (500, 0)

        return list(_map.values()).count(3)

    def part2(self, data):
        sand = (500, 0)

        _map = defaultdict(int)
        _map[sand] = 2

        for line in data:
            coords = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
            for i in range(len(coords) - 1):
                if coords[i][0] == coords[i + 1][0]:
                    a, b = coords[i][1], coords[i + 1][1]
                    if a > b:
                        a, b = b, a
                    for j in range(a, b + 1):
                        _map[(coords[i][0], j)] = 1
                else:
                    a, b = coords[i][0], coords[i + 1][0]
                    if a > b:
                        a, b = b, a
                    for j in range(a, b + 1):
                        _map[(j, coords[i][1])] = 1

        ground = max([i[1] for i in _map.keys()]) + 2

        while _map[(500, 0)] != 3:
            next_sands = [(sand[0], sand[1] + 1), (sand[0] - 1, sand[1] + 1), (sand[0] + 1, sand[1] + 1)]
            for next_sand in next_sands:
                if next_sand[1] < ground and _map[next_sand] == 0:
                    _map[sand] = 0
                    _map[next_sand] = 2
                    sand = next_sand
                    break
            else:
                _map[sand] = 3
                sand = (500, 0)

        return list(_map.values()).count(3)
