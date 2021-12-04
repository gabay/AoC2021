import time

import pyperclip


def count_increases(l):
    increases = 0
    for a, b in zip(l, l[1:]):
        if a < b:
            increases += 1
    return increases

def task1(data):
    numbers = list(map(int, data.strip().split()))
    return count_increases(numbers)

def task2(data):
    numbers = list(map(int, data.strip().split()))
    sums = list(map(sum, zip(numbers, numbers[1:], numbers[2:])))
    return count_increases(sums)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
