from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        nums = {}
        opes = {}

        for line in data:
            key, ope = line.split(": ")
            if ope.isnumeric():
                nums[key] = int(ope)
            else:
                opes[key] = ope.split(" ")

        while "root" in opes:
            del_keys = []

            for key, (x, o, y) in opes.items():
                if type(x) is str:
                    if x in nums:
                        x = nums[x]
                    elif x.isnumeric():
                        x = int(x)

                if type(y) is str:
                    if y in nums:
                        y = nums[y]
                    elif y.isnumeric():
                        y = int(y)

                if type(x) is int and type(y) is int:
                    match o:
                        case "+":
                            nums[key] = x + y
                        case "*":
                            nums[key] = x * y
                        case "-":
                            nums[key] = x - y
                        case "/":
                            nums[key] = x // y
                    del_keys.append(key)
                else:
                    opes[key] = [x, o, y]

            for key in del_keys:
                del opes[key]

        return nums["root"]

    def part2(self, data):
        nums = {}
        opes = {}

        for line in data:
            key, ope = line.split(": ")

            if key == "humn":
                continue

            if ope.isnumeric():
                nums[key] = int(ope)
            else:
                opes[key] = ope.split(" ")

        replace = True
        while replace:
            del_keys = []
            replace = False

            for key, (x, o, y) in opes.items():
                if type(x) is str:
                    if x in nums:
                        x = nums[x]
                        replace = True
                    elif x.isnumeric():
                        x = int(x)

                if type(y) is str:
                    if y in nums:
                        y = nums[y]
                        replace = True
                    elif y.isnumeric():
                        y = int(y)

                if type(x) is int and type(y) is int:
                    match o:
                        case "+":
                            nums[key] = x + y
                        case "-":
                            nums[key] = x - y
                        case "*":
                            nums[key] = x * y
                        case "/":
                            nums[key] = x // y
                    del_keys.append(key)
                    replace = True
                else:
                    opes[key] = (x, o, y)

            for key in del_keys:
                del opes[key]

        x, o, y = opes["root"]
        if type(x) is int:
            x, y = y, x

        start = x
        num = y

        while start != "humn":
            x, o, y = opes[start]
            if type(x) == str:
                match o:
                    case "+":
                        num -= y
                    case "-":
                        num += y
                    case "*":
                        num //= y
                    case "/":
                        num *= y
                start = x
            else:
                match o:
                    case "+":
                        num -= x
                    case "-":
                        num = x - num
                    case "*":
                        num //= x
                    case "/":
                        num = x // num
                start = y

        return num
