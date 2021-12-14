import time
from collections import Counter

import pyperclip


def calc_fish(fish, days):
    day_to_duplicate = Counter(fish)
    for i in range(days):
        if i in day_to_duplicate:
            day_to_duplicate[i + 7] += day_to_duplicate[i]
            day_to_duplicate[i + 9] += day_to_duplicate[i]
            del day_to_duplicate[i]
    return sum(day_to_duplicate.values())

def task1(data):
    fish = list(map(int, data.strip().split(',')))
    return calc_fish(fish, 80)

def task2(data):
    fish = list(map(int, data.strip().split(',')))
    return calc_fish(fish, 256)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
