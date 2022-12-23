from utils.solution_base import SolutionBase
import re


class Solution(SolutionBase):
    def part1(self, data):
        self.check_is_raw()
        face = 1 + 0j

        # ((y, x), facing number, map label), order in UDLR
        facing = {
            0 - 1j: ((-1, 0), 3, "^"),  # facing up
            0 + 1j: ((1, 0), 1, "v"),  # facing down
            -1 + 0j: ((0, -1), 2, "<"),  # facing left
            1 + 0j: ((0, 1), 0, ">"),  # facing right
        }

        desc = self.parse_desc(data[-1])
        _map = self.parse_map(data[:-2])

        pos = (0, _map[0].index("."))  # (y, x)
        _map[pos[0]][pos[1]] = facing[face][2]

        while desc:
            ope = desc.pop(0)

            if ope.isnumeric():
                ope = int(ope)
                dy, dx = facing[face][0]
                for _ in range(ope):
                    y = pos[0] + dy
                    x = pos[1] + dx
                    if y < 0 or y >= len(_map) or x < 0 or x >= len(_map[y]) or _map[y][x] == " ":
                        # move to otherside
                        if face == 1 + 0j:  # facing R
                            # move to leftmost
                            x = [i for i, v in enumerate(_map[y]) if v != " "][0]
                        elif face == -1 + 0j:  # facing L
                            # move to rightmost
                            x = [i for i, v in enumerate(_map[y]) if v != " "][-1]
                        elif face == 0 - 1j:  # facing U
                            # move to downmost
                            col = [row[x] for row in _map]
                            y = [i for i, v in enumerate(col) if v != " "][-1]
                        elif face == 0 + 1j:  # facing D
                            # move to upmost
                            col = [row[x] for row in _map]
                            y = [i for i, v in enumerate(col) if v != " "][0]

                    if _map[y][x] == "#":
                        break
                    else:
                        pos = (y, x)
                        _map[y][x] = facing[face][2]
            else:
                if ope == "L":
                    face *= -1j
                elif ope == "R":
                    face *= 1j
                _map[pos[0]][pos[1]] = facing[face][2]

        r = pos[0] + 1
        c = pos[1] + 1

        # self.print_map(_map)

        return 1000 * r + 4 * c + facing[face][1]

    def part2(self, data):
        self.check_is_raw()
        face = 1 + 0j

        # ((y, x), facing number, map label), order in UDLR
        facing = {
            0 - 1j: ((-1, 0), 3, "^"),  # facing up
            0 + 1j: ((1, 0), 1, "v"),  # facing down
            -1 + 0j: ((0, -1), 2, "<"),  # facing left
            1 + 0j: ((0, 1), 0, ">"),  # facing right
        }

        rotate_to = {
            0 - 1j: "D",  # facing up, turn down
            0 + 1j: "U",  # facing down, turn up
            -1 + 0j: "R",  # facing left, turn right
            1 + 0j: "L",  # facing right, turn left
        }

        desc = self.parse_desc(data[-1])

        cubesize = 4 if data[-1] == "10R5L5R10L4R5L5" else 50
        cube, blocks, blocks_index, rotate = self.parse_cube(data[:-2], cubesize)

        pos = (0, 0)  # (y, x)
        blocks[cube[0][1]][pos[0]][pos[1]] = facing[face][2]

        while desc:
            ope = desc.pop(0)

            if ope.isnumeric():
                ope = int(ope)
                dy, dx = facing[face][0]
                for _ in range(ope):
                    y = pos[0] + dy
                    x = pos[1] + dx

                    test_cube = cube
                    test_rotate = [0 if i is not None else None for i in rotate]
                    test_blocks = [[[i for i in row] for row in block] for block in blocks]

                    if y < 0 or y >= cubesize or x < 0 or x >= cubesize:
                        # turn the cube
                        test_cube, test_rotate = self.rotate_cube(cube, rotate, rotate_to[face])
                        for i, r in enumerate(test_rotate):
                            if r is not None and r != 0:
                                test_blocks[i] = self.rotate_block(blocks[i], r)

                        if face == 1 + 0j:  # facing R
                            # turn left, make the right side to the front
                            x = 0
                        elif face == -1 + 0j:  # facing L
                            # turn right, make the left side to the front
                            x = cubesize - 1
                        elif face == 0 - 1j:  # facing U
                            # turn down, make the up side to the front
                            y = cubesize - 1
                        elif face == 0 + 1j:  # facing D
                            # turn up, make the down side to the front
                            y = 0

                    if blocks[test_cube[0][1]][y][x] == "#":
                        break
                    else:
                        cube = test_cube
                        blocks = test_blocks
                        rotate = [None if a is None else a + b for a, b in zip(rotate, test_rotate)]
                        pos = (y, x)
                        blocks[cube[0][1]][y][x] = facing[face][2]
            else:
                if ope == "L":
                    face *= -1j
                elif ope == "R":
                    face *= 1j
                blocks[cube[0][1]][pos[0]][pos[1]] = facing[face][2]

        blocks[cube[0][1]][pos[0]][pos[1]] = "@"  # mark the final position

        final_block_index = None
        for i, block in enumerate(blocks):
            for row in block:
                if "@" in row:
                    final_block_index = i
                    break

        block_rotate = rotate[final_block_index] % 4
        final_block = self.rotate_block(blocks[final_block_index], -block_rotate)

        x = None
        y = None
        for i, row in enumerate(final_block):
            if "@" in row:
                y = i
                x = row.index("@")
                break

        r = (final_block_index // len(blocks_index[0])) * cubesize + y + 1
        c = (final_block_index % len(blocks_index[0])) * cubesize + x + 1
        xface = (facing[face][1] + 4 - block_rotate) % 4

        return 1000 * r + 4 * c + xface

    def parse_desc(self, desc):
        return re.split(r"(\D+)", desc)

    def parse_map(self, _map):
        max_len = max([len(row) for row in _map])
        return [list(row.ljust(max_len, " ")) for row in _map]

    def print_map(self, _map):
        for r in _map:
            print(*r, sep="")

    def parse_cube(self, _map, size):
        _map = self.parse_map(_map)

        count_h = len(_map[0]) // size
        count_v = len(_map) // size

        blocks = [[_map[y * size + i][x * size : x * size + size] for i in range(size)] for y in range(count_v) for x in range(count_h)]
        blocks_index = [[-1 if block[0][0] == " " else idx + i for i, block in enumerate(blocks[idx : idx + count_h])] for idx in range(0, count_h * count_v, count_h)]

        ref_index = [i for i in blocks_index[0] if i != -1][0]

        """
        transform the tiles to the shape, keep the relation between the tiles:
        [#][S][#] S mean the starting tile
        [.][#][.]
        [.][#][.]
        [.][#][.]
        """
        rotate = []
        for row_id, row_blocks in enumerate(blocks_index):
            for col_id, block_id in enumerate(row_blocks):
                if block_id == -1:
                    rotate.append(None)
                elif col_id == ref_index:
                    rotate.append(0)
                else:
                    f = 1 if col_id < ref_index else -1
                    r = (row_id + abs(ref_index - col_id) - 1) * f
                    if row_id - f * r < 0 or abs(r) == 3:
                        r = (4 - abs(r)) * -f
                    rotate.append(r)

        cube = [[-1] * count_h for _ in range(4)]

        for i, row in enumerate(blocks_index):
            for j, v in enumerate(row):
                if v == -1:
                    continue
                else:
                    idx = i * count_h + j
                    r = rotate[idx]

                    y = i
                    x = j

                    if abs(x - ref_index) == 1 and y < 3:
                        y = 0
                    elif x != ref_index:
                        y = 3
                        x = ref_index

                    cube[y][x] = v
                    blocks[v] = self.rotate_block(blocks[v], r)

        if count_h > 3:
            if cube[0][0] == -1:
                cube = [i[1:] for i in cube]
            else:
                cube = [i[:-1] for i in cube]

        return cube, blocks, blocks_index, rotate

    def rotate_block(self, block, r):
        if r == 0:
            return block
        elif r == 1:
            return [list(i) for i in zip(*block[::-1])]
        elif r == -1:
            return [list(i) for i in zip(*block)][::-1]
        elif r == 2 or r == -2:
            return [i[::-1] for i in block[::-1]]

    def rotate_cube(self, cube, rotate, direction):
        cube2 = [[i for i in row] for row in cube]
        rotate2 = [None if i is None else 0 for i in rotate]

        if direction == "U":
            cube2 = [[cube2[0][0], cube2[1][1], cube2[0][2]], [-1, cube2[2][1], -1], [-1, cube2[3][1], -1], [-1, cube2[0][1], -1]]
            rotate2[cube2[0][0]] -= 1
            rotate2[cube2[0][2]] += 1
        elif direction == "D":
            cube2 = [[cube2[0][0], cube2[3][1], cube2[0][2]], [-1, cube2[0][1], -1], [-1, cube2[1][1], -1], [-1, cube2[2][1], -1]]
            rotate2[cube2[0][0]] += 1
            rotate2[cube2[0][2]] -= 1
        elif direction == "L":
            cube2 = [[cube2[0][1], cube2[0][2], cube2[2][1]], [-1, cube2[1][1], -1], [-1, cube2[0][0], -1], [-1, cube2[3][1], -1]]
            rotate2[cube2[0][2]] += 2
            rotate2[cube2[1][1]] -= 1
            rotate2[cube2[2][1]] += 2
            rotate2[cube2[3][1]] += 1
        elif direction == "R":
            cube2 = [[cube2[2][1], cube2[0][0], cube2[0][1]], [-1, cube2[1][1], -1], [-1, cube2[0][2], -1], [-1, cube2[3][1], -1]]
            rotate2[cube2[0][0]] += 2
            rotate2[cube2[1][1]] += 1
            rotate2[cube2[2][1]] += 2
            rotate2[cube2[3][1]] -= 1

        return cube2, rotate2
