import time

import pyperclip


def lowpoints(points):
    for y, row in enumerate(points):
        for x, point in enumerate(row):
            if y > 0 and points[y-1][x] <= point:
                continue
            if y + 1 < len(points) and points[y+1][x] <= point:
                continue
            if x > 0 and row[x-1] <= point:
                continue
            if x + 1 < len(row) and row[x+1] <= point:
                continue
            yield y, x, point

def task1(data):
    points = [list(map(int, line)) for line in data.strip().splitlines()]
    result = 0
    for _, _, point in lowpoints(points):
        result += point + 1
    return result

def get_basin_at(points, y0, x0):
    pending = [(y0, x0)]
    basin = set()
    while pending:
        y, x = pending.pop()
        if (y, x) in basin:
            continue
        if not (0 <= x < len(points[0]) and 0 <= y < len(points)):
            continue
        point = points[y][x]
        if point == 9:
            continue
        basin.add((y, x))
        pending += [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    return basin

def get_basins(points):
    points_in_basin = set()
    for y, row in enumerate(points):
        for x, point in enumerate(row):
            if (y, x) in points_in_basin:
                continue
            if point == 9:
                continue
            basin = get_basin_at(points, y, x)
            yield basin
            points_in_basin |= basin


def task2(data):
    points = [list(map(int, line)) for line in data.strip().splitlines()]
    basins = list(get_basins(points))
    basin_sizes = [len(basin) for basin in basins]
    a, b, c = sorted(basin_sizes)[-3:]
    return a * b * c

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
