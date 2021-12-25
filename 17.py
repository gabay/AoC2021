from __future__ import annotations

import re
import time
from dataclasses import dataclass
from functools import reduce
from typing import List, Optional

import pyperclip


def peak(y):
    if y >= 0:
        return (y * (y + 1)) // 2

def parse_data(data):
    x1, x2 = map(int, re.search(r"x\=(\d+)\.\.(\d+)", data).groups())
    y1, y2 = map(int, re.search(r"y\=(\-?\d+)\.\.(\-?\d+)", data).groups())
    return x1, x2, y1, y2

def reaches_target(x, y, target):
    x1, x2, y1, y2 = target
    xx, yy = 0, 0
    while xx <= x2 and yy >= y1:
        xx += x
        yy += y
        if x > 0:
            x -= 1
        y -= 1
        if x1 <= xx <=  x2 and y1 <= yy <= y2:
            return True
    return False

def task1(data):
    target = parse_data(data)
    for y in range(1000, 0, -1):
        for x in range(1000):
            if reaches_target(x, y, target):
                print(x, y)
                return peak(y)

def task2(data):
    target = parse_data(data)
    velocities = 0
    for y in range(1000, 0, -1):
        for x in range(1000):
            if reaches_target(x, y, target):
                velocities += 1
    return velocities

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
