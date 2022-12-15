from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        pairs = [tuple(map(lambda item: tuple(map(lambda x: int(x[2:]), item.replace(",", "").split()[-2:])), line.split(": "))) for line in data]
        target_y = 10 if pairs[0] == ((2, 18), (-2, 15)) else 2000000

        x_ranges = []
        for pair in pairs:
            distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
            diff_x = distance - abs(target_y - pair[0][1])
            if diff_x >= 0:
                x_ranges.append((pair[0][0] - diff_x, pair[0][0] + diff_x))

        x_ranges.sort()

        coverage = x_ranges[0]
        empty = []
        for i in range(1, len(x_ranges)):
            if x_ranges[i][0] <= coverage[1]:
                coverage = (coverage[0], max(coverage[1], x_ranges[i][1]))
            else:
                empty.extend(list(range(coverage[1] + 1, x_ranges[i][0])))

        num_sensors = len(set([i[0] for i in pairs if i[0][1] == target_y and coverage[0] <= i[0][0] <= coverage[1]]))
        num_beacons = len(set([i[1] for i in pairs if i[1][1] == target_y and coverage[0] <= i[1][0] <= coverage[1]]))

        return (coverage[1] - coverage[0] + 1) - num_sensors - num_beacons - len(empty)

    def part2(self, data):
        pairs_temp = [tuple(map(lambda item: tuple(map(lambda x: int(x[2:]), item.replace(",", "").split()[-2:])), line.split(": "))) for line in data]
        pairs = [(sensor, beacon, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])) for sensor, beacon in pairs_temp]
        target_ys = 20 if pairs[0] == ((2, 18), (-2, 15)) else 4000000

        for target_y in range(target_ys + 1):
            x_ranges = []
            for sensor, _, distance in pairs:
                diff_x = distance - abs(target_y - sensor[1])
                if diff_x >= 0:
                    x_ranges.append((sensor[0] - diff_x, sensor[0] + diff_x))

            x_ranges.sort()

            coverage = x_ranges[0]
            for i in range(1, len(x_ranges)):
                if x_ranges[i][0] <= coverage[1]:
                    coverage = (coverage[0], max(coverage[1], x_ranges[i][1]))
                else:
                    # print("position:", (coverage[1] + 1, target_y))
                    return (coverage[1] + 1) * 4000000 + target_y
