import time
from queue import PriorityQueue

import pyperclip


class RiskMap:
    def __init__(self, risks):
        self.risks = risks
        self.x = len(risks[0])
        self.y = len(risks)

    def __getitem__(self, xy):
        x, y = xy
        additions = x // self.x + y // self.y
        result = self.risks[y % self.y][x % self.x] + additions
        if result > 9:
            result -= 9
        return result

def points_around(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def path_of_lowest_risk(risk_map, target_x, target_y):
    queue = PriorityQueue()
    queue.put((0, 0, 0))
    seen = set((0, 0))
    while queue:
        risk, x, y = queue.get()
        if x == target_x and y == target_y:
            return risk

        for xx, yy in points_around(x, y):
            if 0 <= xx <= target_x and 0 <= yy <= target_y and (xx, yy) not in seen:
                queue.put((risk + risk_map[xx, yy], xx, yy))
                seen.add((xx, yy))

def task1(data):
    risks = [[int(i) for i in line] for line in data.splitlines()]
    risk_map = RiskMap(risks)
    return path_of_lowest_risk(risk_map, risk_map.x - 1, risk_map.y - 1)

def task2(data):
    risks = [[int(i) for i in line] for line in data.splitlines()]
    risk_map = RiskMap(risks)
    return path_of_lowest_risk(risk_map, risk_map.x * 5 - 1, risk_map.y * 5 - 1)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
