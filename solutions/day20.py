from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        coords = [(idx, int(item)) for idx, item in enumerate(data)]
        _len = len(coords)

        for i in range(_len):
            pos = [p for p, coord in enumerate(coords) if coord[0] == i][0]
            coord = coords[pos]
            new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

            coord = coords.pop(pos)
            coords.insert(new_pos, coord)

        zero_pos = [p for p, item in enumerate(coords) if item[1] == 0][0]

        return coords[(zero_pos + 1000) % _len][1] + coords[(zero_pos + 2000) % _len][1] + coords[(zero_pos + 3000) % _len][1]

    def part2(self, data):
        # there must be a better way to solve this, but my brain fried, so optimize later (maybe)

        key = 811589153
        coords = [(idx, int(item) * key) for idx, item in enumerate(data)]
        _len = len(coords)

        for _ in range(10):
            for i in range(_len):
                pos = [p for p, coord in enumerate(coords) if coord[0] == i][0]
                coord = coords[pos]
                new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

                coord = coords.pop(pos)
                coords.insert(new_pos, coord)

        zero_pos = [p for p, item in enumerate(coords) if item[1] == 0][0]

        return coords[(zero_pos + 1000) % _len][1] + coords[(zero_pos + 2000) % _len][1] + coords[(zero_pos + 3000) % _len][1]
