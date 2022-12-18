from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        droplets = set([tuple(map(int, line.split(","))) for line in data])
        sides = 0
        neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

        for x, y, z in droplets:
            neighbor_droplets = [(x + dx, y + dy, z + dz) for dx, dy, dz in neighbors]
            sides += len([1 for nd in neighbor_droplets if nd not in droplets])

        return sides

    def part2(self, data):
        droplets = set([tuple(map(int, line.split(","))) for line in data])
        sides = 0
        neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

        # min_x = min(d[0] for d in droplets)
        # max_x = max(d[0] for d in droplets)
        # min_y = min(d[1] for d in droplets)
        # max_y = max(d[1] for d in droplets)
        # min_z = min(d[2] for d in droplets)
        # max_z = max(d[2] for d in droplets)
        min_x, max_x = self.minmax(d[0] for d in droplets)
        min_y, max_y = self.minmax(d[1] for d in droplets)
        min_z, max_z = self.minmax(d[2] for d in droplets)

        # add 1 to the range to account for the air cube just outside the droplets
        x_range = range(min_x - 1, max_x + 2)
        y_range = range(min_y - 1, max_y + 2)
        z_range = range(min_z - 1, max_z + 2)

        start = (min_x - 1, min_y - 1, min_z - 1)  # start at the air cube just outside the droplets
        queue = [start]
        seen = set() | droplets  # only have to check air cubes, so ignore the lava cubes

        while queue:
            x, y, z = queue.pop(0)

            if (x, y, z) in seen:
                continue

            seen.add((x, y, z))
            neighbor_droplets = [(x + dx, y + dy, z + dz) for dx, dy, dz in neighbors]
            sides += len([1 for nd in neighbor_droplets if nd in droplets])

            for nd in neighbor_droplets:
                if nd not in seen and nd[0] in x_range and nd[1] in y_range and nd[2] in z_range:
                    queue.append(nd)

        return sides

    def minmax(self, _list):
        _list = list(_list)
        _min = _list[0]
        _max = _list[0]
        for i in _list[1:]:
            if i < _min:
                _min = i
            elif i > _max:
                _max = i
        return _min, _max
