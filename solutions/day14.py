from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        sand_pos = (500, 0)

        rock = self.parse_data(data)
        rest = set()

        max_depth = max(i[1] for i in rock)
        falls = [(0, 1), (-1, 1), (1, 1)]

        while sand_pos[1] < max_depth:
            for fall in falls:
                next_sand_pos = (sand_pos[0] + fall[0], sand_pos[1] + fall[1])
                if next_sand_pos not in rock and next_sand_pos not in rest:
                    sand_pos = next_sand_pos
                    break
            else:
                rest.add(sand_pos)
                sand_pos = (500, 0)

        return len(rest)

    def part2(self, data):
        sand_pos = (500, 0)

        rock = self.parse_data(data)
        rest = set()

        ground = max(i[1] for i in rock) + 2
        falls = [(0, 1), (-1, 1), (1, 1)]

        while (500, 0) not in rest:
            for fall in falls:
                next_sand_pos = (sand_pos[0] + fall[0], sand_pos[1] + fall[1])
                if next_sand_pos not in rock and next_sand_pos not in rest and next_sand_pos[1] < ground:
                    sand_pos = next_sand_pos
                    break
            else:
                rest.add(sand_pos)
                sand_pos = (500, 0)

        return len(rest)

    def parse_data(self, data):
        rock = set()

        for line in data:
            coords = [tuple(map(int, i.split(","))) for i in line.split(" -> ")]
            for i in range(len(coords) - 1):
                if coords[i][0] == coords[i + 1][0]:
                    a, b = sorted([coords[i][1], coords[i + 1][1]])
                    for j in range(a, b + 1):
                        rock.add((coords[i][0], j))
                else:
                    a, b = sorted([coords[i][0], coords[i + 1][0]])
                    for j in range(a, b + 1):
                        rock.add((j, coords[i][1]))

        return rock
