from __future__ import annotations

import json
import re
import time
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple

import pyperclip


def parse_data(data) -> List[List]:
    key, pixels = data.strip().split('\n\n')
    key = [1 if k == '#' else 0 for k in key]
    pixels = [[1 if pixel == '#' else 0 for pixel in line] for line in pixels.splitlines()]
    return key, pixels

def pixel_at(pixels, background, x, y):
    if pixels and 0 <= x < len(pixels[0]) and 0 <= y < len(pixels):
        return pixels[y][x]
    return background

def value_at(pixels, background, x, y):
    value = 0
    for yy in (y-1,y,y+1):
        for xx in (x-1,x,x+1):
            value = value * 2 + pixel_at(pixels, background, xx, yy)
    return value

def flip(key, pixels, background):
    new_pixels = []
    for y in range(-1, len(pixels) + 1):
        new_pixels.append([])
        for x in range(-1, len(pixels[0]) + 1):
            value = value_at(pixels, background, x, y)
            new_pixels[-1].append(key[value])
    new_background = key[value_at([], background, 0, 0)]
    return new_pixels, new_background

def task1(data):
    key, pixels = parse_data(data)
    background = 0
    pixels, background = flip(key, pixels, background)
    pixels, background = flip(key, pixels, background)
    return sum(pixels, []).count(1)

def task2(data):
    key, pixels = parse_data(data)
    background = 0
    for _ in range(50):
        pixels, background = flip(key, pixels, background)
    return sum(pixels, []).count(1)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
