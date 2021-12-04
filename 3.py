import time
from collections import Counter

import pyperclip


def task1(data):
    numbers = data.strip().splitlines()
    g = 0
    e = 0
    for bits in zip(*numbers):
        counter = Counter(bits)
        most_common = int(counter.most_common()[0][0])
        least_common = int(counter.most_common()[1][0])
        g = (g * 2) + most_common
        e = (e * 2) + least_common
    return g * e

def split_by_index(numbers, index):
    numbers_with_0 = [n for n in numbers if n[index] == '0']
    numbers_with_1 = [n for n in numbers if n[index] == '1']
    return numbers_with_0, numbers_with_1

def task2(data):
    numbers = data.strip().splitlines()
    ox_candidates = numbers
    for index in range(0, len(numbers[0])):
        numbers_0, numbers_1 = split_by_index(ox_candidates, index)
        ox_candidates = numbers_1 if len(numbers_1) >= len(numbers_0) else numbers_0
        if len(ox_candidates) == 1:
            break

    co_candidates = numbers
    for index in range(0, len(numbers[0])):
        numbers_0, numbers_1 = split_by_index(co_candidates, index)
        co_candidates = numbers_0 if len(numbers_1) >= len(numbers_0) else numbers_1
        if len(co_candidates) == 1:
            break
    return int(ox_candidates[0], 2) * int(co_candidates[0], 2)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
