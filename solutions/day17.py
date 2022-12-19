from utils.solution_base import SolutionBase
from itertools import zip_longest


class Solution(SolutionBase):
    def part1(self, data):
        jets = data[0]
        jet_len = len(jets)
        jet_idx = 0

        above = 3

        # fmt: off
        rocks = [
            [
                [0, 0, 1, 1, 1, 1, 0]   # ..####.
            ],
            [
                [0, 0, 0, 1, 0, 0, 0],  # ...#...
                [0, 0, 1, 1, 1, 0, 0],  # ..###..
                [0, 0, 0, 1, 0, 0, 0]   # ...#...
            ],
            [
                [0, 0, 1, 1, 1, 0, 0],  # ..###..
                [0, 0, 0, 0, 1, 0, 0],  # ....#..
                [0, 0, 0, 0, 1, 0, 0]   # ....#..
            ],
            [
                [0, 0, 1, 0, 0, 0, 0],  # ..#....
                [0, 0, 1, 0, 0, 0, 0],  # ..#....
                [0, 0, 1, 0, 0, 0, 0],  # ..#....
                [0, 0, 1, 0, 0, 0, 0]   # ..#....
            ],
            [
                [0, 0, 1, 1, 0, 0, 0],  # ..##...
                [0, 0, 1, 1, 0, 0, 0]   # ..##...
            ],
        ]
        # fmt: on
        rock_idx = 0

        self.room = [[1, 1, 1, 1, 1, 1, 1]]

        while rock_idx < 2022:
            self.room += [[0, 0, 0, 0, 0, 0, 0] for _ in range(above)]
            self.rock = rocks[rock_idx % 5]

            height = len(self.room)

            while 1:
                # push by jet
                org_rock = self.rock
                jet = jets[jet_idx]
                self.rock_push(jet)
                if self.check_overlap(height):
                    self.rock = org_rock
                jet_idx = (jet_idx + 1) % jet_len

                # falling
                height -= 1
                if self.check_overlap(height):
                    height += 1
                    self.rock_stop(height)
                    rock_idx += 1
                    break

        # self.print_room()
        return len(self.room) - 1

    def part2(self, data):
        jets = data[0]
        jet_len = len(jets)
        jet_idx = 0

        above = 3

        # fmt: off
        rocks = [
            [
                [0, 0, 1, 1, 1, 1, 0]   # ..####.
            ],
            [
                [0, 0, 0, 1, 0, 0, 0],  # ...#...
                [0, 0, 1, 1, 1, 0, 0],  # ..###..
                [0, 0, 0, 1, 0, 0, 0]   # ...#...
            ],
            [
                [0, 0, 1, 1, 1, 0, 0],  # ..###..
                [0, 0, 0, 0, 1, 0, 0],  # ....#..
                [0, 0, 0, 0, 1, 0, 0]   # ....#..
            ],
            [
                [0, 0, 1, 0, 0, 0, 0],  # ..#....
                [0, 0, 1, 0, 0, 0, 0],  # ..#....
                [0, 0, 1, 0, 0, 0, 0],  # ..#....
                [0, 0, 1, 0, 0, 0, 0]   # ..#....
            ],
            [
                [0, 0, 1, 1, 0, 0, 0],  # ..##...
                [0, 0, 1, 1, 0, 0, 0]   # ..##...
            ],
        ]
        # fmt: on
        rock_idx = 0

        self.room = [[1, 1, 1, 1, 1, 1, 1]]

        self.check_depth = 10
        self.states = {}
        self.state_history = []

        self._break = False

        # turns out it has repeated pattern
        # find the repeat and do the math
        while 1:
            if self._break:
                break

            org_height = len(self.room)

            self.room += [[0, 0, 0, 0, 0, 0, 0] for _ in range(above)]
            self.rock = rocks[rock_idx % 5]

            height = len(self.room)

            while 1:
                # push by jet
                org_rock = self.rock
                jet = jets[jet_idx]
                self.rock_push(jet)
                if self.check_overlap(height):
                    self.rock = org_rock
                jet_idx = (jet_idx + 1) % jet_len

                # falling
                height -= 1
                if self.check_overlap(height):
                    height += 1
                    self.rock_stop(height)
                    self.check_state_history(rock_idx, jet_idx, org_height)
                    rock_idx += 1
                    break

        repeated = self.state_history[-1]
        round_start = self.state_history.index(repeated)
        round_len = len(self.state_history) - round_start - 1

        round_height_diff_sum = 0
        for i in range(round_start, round_start + round_len):
            state = self.state_history[i]
            round_height_diff_sum += self.states[state]

        tower_height = 0
        rocks = 1000000000000

        tower_height = sum(self.states[self.state_history[i]] for i in range(min(round_start, rocks)))

        if rocks > round_start:
            after_repeat = rocks - round_start
            rounds = after_repeat // round_len
            left_rocks = after_repeat % round_len

            tower_height += round_height_diff_sum * rounds
            tower_height += sum(self.states[self.state_history[round_start + i]] for i in range(left_rocks))

        return tower_height

    def rock_push(self, push):
        rock = self.rock
        if push == ">":
            check = sum([i[-1] for i in rock])
            if check == 0:
                rock = [[0] + i[:-1] for i in rock]
        else:
            check = sum([i[0] for i in rock])
            if check == 0:
                rock = [i[1:] + [0] for i in rock]
        self.rock = rock

    def check_overlap(self, height):
        rock = [[0, 0, 0, 0, 0, 0, 0] for _ in range(height)] + self.rock
        full_height = height + len(self.rock)

        room = self.room
        if len(room) > full_height:
            room = room[:full_height]
        else:
            room += [[0, 0, 0, 0, 0, 0, 0] for _ in range(full_height - len(room))]

        for i in range(full_height - 1, -1, -1):
            roomline = room[i]
            rockline = rock[i]
            if sum(rockline) == 0:
                return False
            for x, y in zip(roomline, rockline):
                if x + y > 1:
                    return True
        return False

    def rock_stop(self, height):
        room = self.room
        rock = [[0, 0, 0, 0, 0, 0, 0] for _ in range(height)] + self.rock

        new_room = []
        for roomline, rockline in zip_longest(room, rock, fillvalue=[0, 0, 0, 0, 0, 0, 0]):
            new_room_line = []
            for x, y in zip(roomline, rockline):
                new_room_line.append(x + y)
            new_room.append(new_room_line)
        while sum(new_room[-1]) == 0:
            new_room.pop()
        self.room = new_room

    def check_state_history(self, rock_idx, jet_idx, height):
        line_num = min(len(self.room), self.check_depth)

        scan = "".join(str(i) for line in self.room[-line_num:] for i in line)
        state = (rock_idx % 5, jet_idx, scan)

        height_diff = len(self.room) - height

        if state in self.states:
            self.state_history += [state]
            self._break = True
        else:
            self.states[state] = height_diff
            self.state_history += [state]

    def print_room(self):
        room = self.room[::-1]
        for r in room:
            print(*r, sep="")
        print()
