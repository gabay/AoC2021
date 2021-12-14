import time

import pyperclip


def task1(data):
    positions = sorted(map(int, data.strip().split(',')))
    median = positions[len(positions) // 2]
    fuel = sum(abs(position - median) for position in positions)
    return fuel

def fuel_cost2(distance):
    return (distance**2 + distance) // 2

def fuel_cost_for_position2(positions, suggested_average):
    return sum(map(fuel_cost2, [abs(p - suggested_average) for p in positions]))

def cheapest_position2(positions):
    p1, p2 = min(positions), max(positions)
    while True:
        p = (p1 + p2) // 2
        fuel_costs = [fuel_cost_for_position2(positions, avg) for avg in [p - 1, p, p + 1]]
        if fuel_costs[0] < fuel_costs[1]:
            p2 = p
        elif fuel_costs[1] > fuel_costs[2]:
            p1 = p
        else:
            return fuel_costs[1]

def task2(data):
    positions = sorted(map(int, data.strip().split(',')))
    return cheapest_position2(positions)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
