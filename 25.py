from __future__ import annotations

import itertools
import time

import pyperclip


def right_movable_cucumbers(m):
    for y, row in enumerate(m):
        for x, cell in enumerate(row):
            new_x = (x+1) % len(row)
            if cell == '>' and row[new_x] == '.':
                yield x, y, new_x, y

def down_movable_cucumbers(m):
    for y, row in enumerate(m):
        new_y = (y+1) % len(m)
        for x, cell in enumerate(row):
            if cell == 'v' and m[new_y][x] == '.':
                yield x, y, x, new_y

def step(m):
    moves = 0
    for x, y, new_x, new_y in list(right_movable_cucumbers(m)):
        moves += 1
        m[y][x], m[new_y][new_x] = '.', '>'
    for x, y, new_x, new_y in list(down_movable_cucumbers(m)):
        moves += 1
        m[y][x], m[new_y][new_x] = '.', 'v'
    return moves

def parse_data(data):
    return [[c for c in line] for line in data.splitlines()]

def task1(data):
    m = parse_data(data)
    for i in itertools.count(1):
        moves = step(m)
        if moves == 0:
            return i

def main():
    start_time = time.time()
    answer = task1(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
