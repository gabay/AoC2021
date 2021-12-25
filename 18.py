from __future__ import annotations

import itertools
import json
import time
from copy import deepcopy
from functools import reduce
from typing import List

import pyperclip


def sn_add(a: List, b: List):
    a = deepcopy(a)
    b = deepcopy(b)
    result = [a, b]
    sn_reduce(result)
    return result

def sn_reduce(sn):
    while True:
        if sn_explode(sn):
            continue
        if sn_split(sn):
            continue
        break

def sn_explode(sn):
    for item, path in sn_items_paths(sn):
        if isinstance(item, list) and len(path) == 4:
            sn_explode_at(sn, path)
            return True
    return False

def sn_explode_at(sn, path):
    pair = sn_at(sn, path)
    left_path = path_of_number_to_the_left(sn, path)
    right_path = path_of_number_to_the_right(sn, path)
    if left_path:
        sn_set(sn, left_path, sn_at(sn, left_path) + pair[0])
    if right_path:
        sn_set(sn, right_path, sn_at(sn, right_path) + pair[1])
    sn_set(sn, path, 0)

def sn_at(sn, path):
    if not path:
        return sn
    return sn_at(sn[path[0]], path[1:])

def sn_set(sn, path, value):
    if len(path) == 1:
        sn[path[0]] = value
    else:
        sn_set(sn[path[0]], path[1:], value)

def path_of_number_to_the_left(sn, path):
    path = path.copy()
    while path and path[-1] == 0:
        path.pop()
    if not path:
        return None

    path[-1] = 0
    while not isinstance(sn_at(sn, path), int):
        path.append(1)
    return path

def path_of_number_to_the_right(sn, path):
    path = path.copy()
    while path and path[-1] == 1:
        path.pop()
    if not path:
        return None

    path[-1] = 1
    while not isinstance(sn_at(sn, path), int):
        path.append(0)
    return path

def sn_split(sn):
    for item, path in sn_items_paths(sn):
        if isinstance(item, int) and item >= 10:
            sn_split_at(sn, path)
            return True
    return False

def sn_split_at(sn, path):
    value = sn_at(sn, path)
    sn_set(sn, path, [value // 2, (value + 1) // 2])

def sn_items_paths(sn):
    items = [(sn, [])]
    while items:
        item, path = items.pop()
        yield item, path
        if isinstance(item, list):
            items.append((item[1], path + [1]))
            items.append((item[0], path + [0]))

def magnitude(sn):
    if isinstance(sn, int):
        return sn
    return 3 * magnitude(sn[0]) + 2 * magnitude(sn[1])

def parse_data(data) -> List[List]:
    return [json.loads(line) for line in data.strip().splitlines()]

def task1(data):
    numbers = parse_data(data)
    result = reduce(sn_add, numbers)
    return magnitude(result)

def task2(data):
    numbers = parse_data(data)
    magnitudes = []
    for a, b in itertools.permutations(numbers, 2):
        magnitudes.append(magnitude(sn_add(a, b)))
    return max(magnitudes)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
