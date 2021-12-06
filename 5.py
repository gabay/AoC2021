import re
import time
from collections import Counter

import pyperclip


def parse_data(data):
    lines = []
    for coordinates in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", data):
        lines.append(list(map(int, coordinates)))
    return lines

def points_in_horizontal_or_vertical_line(line):
    x1, y1, x2, y2 = line
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            yield (x1, y)
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield (x, y1)

def points_in_line(line):
    x1, y1, x2, y2 = line
    if x1 == x2 or y1 == y2:
        yield from points_in_horizontal_or_vertical_line(line)
    else:
        for x, y in zip(range(x1, x2, 1 if x2 > x1 else -1), range(y1, y2, 1 if y2 > y1 else -1)):
            yield (x, y)
        yield (x2, y2)


def task1(data):
    lines = parse_data(data)
    points = Counter()
    for line in lines:
        for point in points_in_horizontal_or_vertical_line(line):
            points[point] += 1

    return sum(1 for count in points.values() if count > 1)


def task2(data):
    lines = parse_data(data)
    points = Counter()
    for line in lines:
        for point in points_in_line(line):
            points[point] += 1

    return sum(1 for count in points.values() if count > 1)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
