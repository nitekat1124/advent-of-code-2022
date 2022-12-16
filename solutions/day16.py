from collections import deque
from utils.solution_base import SolutionBase
import networkx as nx


class Solution(SolutionBase):
    def part1(self, data):
        valves, move_cost = self.parse_data(data)

        most_pressure = 0
        queue = deque([("AA", 30, 0, [])])
        while queue:
            location, time_left, pressure, history = queue.pop()

            if pressure > most_pressure:
                most_pressure = pressure

            if time_left <= 0:
                continue

            next_pos = [i for i in valves if i not in history]
            for np in next_pos:
                cost_time = move_cost[(location, np)]
                flow_rate = valves[np]
                current_total_pressure = pressure + (time_left - cost_time - 1) * flow_rate

                close_valves = [i for i in valves if i not in history + [np]]
                remaining_pressure = sum([(time_left - cost_time - 3) * valves[i] for i in close_valves])
                if remaining_pressure + current_total_pressure < most_pressure:
                    continue

                queue.append((np, time_left - cost_time - 1, current_total_pressure, history + [np]))

        return most_pressure

    def part2(self, data):
        valves, move_cost = self.parse_data(data)

        most_pressure = 0
        queue = deque([([(26, "AA"), (26, "AA")], 0, [])])
        while queue:
            location_list, pressure, history = queue.pop()
            time_left, location = location_list.pop(0)

            if pressure > most_pressure:
                most_pressure = pressure

            if time_left <= 0:
                continue

            next_pos = [i for i in valves if i not in history]
            for np in next_pos:
                cost_time = move_cost[(location, np)]
                flow_rate = valves[np]
                next_location_list = location_list + [(time_left - cost_time - 1, np)]
                current_total_pressure = pressure + (time_left - cost_time - 1) * flow_rate

                close_valves = [i for i in valves if i not in history + [np]]
                remaining_pressure = sum([(time_left - cost_time - 3) * valves[i] for i in close_valves])
                if remaining_pressure + current_total_pressure < most_pressure:
                    continue

                queue.append((next_location_list, current_total_pressure, history + [np]))

        return most_pressure

    def parse_data(self, data):
        valves = {}
        move_cost = {}
        g = nx.Graph()

        for line in data:
            tmp1, tmp2 = line.split("; ")
            tmp3 = tmp1.split(" ")
            valve = tmp3[1]
            rate = int(tmp3[-1].split("=")[1])
            to = [i.replace(",", "") for i in tmp2.split(" ")[4:]]

            if rate > 0:
                valves[valve] = rate

            for v in to:
                g.add_edge(valve, v)

        temp = ["AA"] + list(valves.keys())
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                v1 = temp[i]
                v2 = temp[j]
                t = nx.shortest_path_length(g, v1, v2)
                move_cost[(v1, v2)] = move_cost[(v2, v1)] = t

        return valves, move_cost
