import re
import time

import pyperclip


def parse_dots(data):
    dots = re.findall(r'(\d+),(\d+)', data)
    return set((int(x), int(y)) for x, y in dots)

def parse_folds(data):
    folds = re.findall(r'fold along (x|y)\=(\d+)', data)
    return [(axis, int(value)) for axis, value in folds]

def parse_data(data):
    return parse_dots(data), parse_folds(data)

def fold_number(number, fold_value):
    return number if number <= fold_value else 2*fold_value - number

def fold_dot(dot, fold):
    axis, value = fold
    if axis == 'x':
        return (fold_number(dot[0], value), dot[1])
    if axis == 'y':
        return (dot[0], fold_number(dot[1], value))
    raise ValueError(axis)

def fold_dots(dots, fold):
    return set([fold_dot(dot, fold) for dot in dots])

def task1(data):
    dots, folds = parse_data(data)
    new_dots = fold_dots(dots, folds[0])
    return len(new_dots)

def print_dots(dots):
    maxx = max(dot[0] for dot in dots)
    maxy = max(dot[1] for dot in dots)
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            print('#' if (x, y) in dots else '.', end='')
        print()

def task2(data):
    dots, folds = parse_data(data)
    for fold in folds:
        dots = fold_dots(dots, fold)
    print_dots(dots)
    return 0

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
