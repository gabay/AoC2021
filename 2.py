import time

import pyperclip


def task1(data):
    position = 0
    depth = 0
    for line in data.strip().splitlines():
        direction, amount = line.split()
        amount = int(amount)
        if direction == 'forward':
            position += amount
        elif direction == 'down':
            depth += amount
        elif direction == 'up':
            depth -= amount
    return position * depth

def task2(data):
    position = 0
    depth = 0
    aim = 0
    for line in data.strip().splitlines():
        direction, amount = line.split()
        amount = int(amount)
        if direction == 'forward':
            position += amount
            depth += amount * aim
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
    return position * depth

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
