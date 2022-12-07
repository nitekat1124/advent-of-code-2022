from utils.solution_base import SolutionBase
from collections import defaultdict


class Solution(SolutionBase):
    def part1(self, data):
        dirs_size = self.calc_dir_size(data)
        return sum(v for v in dirs_size.values() if v <= 100000)

    def part2(self, data):
        dirs_size = self.calc_dir_size(data)
        unused = 70000000 - dirs_size["/"]
        require = 30000000 - unused
        return min(v for v in dirs_size.values() if v >= require)

    def calc_dir_size(self, data):
        dirs, sub_dirs = self.parse_commands(data)
        dirs_size = defaultdict(int)

        for k, v in dirs.items():
            dirs_size[k] += v
            queue = [k]
            while queue:
                dir = queue.pop(0)
                if dir in sub_dirs:
                    for h in sub_dirs[dir]:
                        dirs_size[k] += dirs[h]
                        queue.append(h)
        return dirs_size

    def parse_commands(self, data):
        idx = 0
        dirs = {"/": 0}
        sub_dirs = defaultdict(list)
        working_dir = []

        while idx < len(data):
            match data[idx][:4]:
                case "$ cd":
                    dir_name = data[idx][5:]
                    match dir_name:
                        case "..":
                            working_dir.pop()
                        case _:
                            working_dir.append(dir_name)
                    idx += 1
                case "$ ls":
                    idx += 1
                    while idx < len(data) and data[idx][0] != "$":
                        type_or_size, dir_name = data[idx].split()
                        curr_dir = "/".join(working_dir)
                        match type_or_size:
                            case "dir":
                                path = f"{curr_dir}/{dir_name}"
                                dirs[path] = 0
                                sub_dirs[curr_dir].append(path)
                            case _:
                                dirs[curr_dir] += int(type_or_size)
                        idx += 1
        return dirs, sub_dirs
