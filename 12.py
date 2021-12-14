import time
from collections import Counter

import pyperclip


def extend_path1(path, adj):
    last_cave = path[-1]
    for next_cave in adj[last_cave]:
        if next_cave.isupper() or next_cave not in path:
            yield path + [next_cave]

def count_pathes_from_start_to_end(adj, extend_function):
    result = 0
    paths = [['start']]
    while paths:
        path = paths.pop()
        for extended_path in extend_function(path, adj):
            if extended_path[-1] == 'end':
                result += 1
            else:
                paths.append(extended_path)
    return result

def task1(data):
    adj = {}
    for line in data.strip().splitlines():
        a, b = line.split('-')
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return count_pathes_from_start_to_end(adj, extend_path1)

def did_visit_small_cave_twice(path):
    counter = Counter(path)
    for cave, visits in counter.items():
        if cave.islower() and visits == 2:
            return True
    return False

def extend_path2(path, adj):
    allowed_small_cave_visits = 1 if did_visit_small_cave_twice(path) else 2
    last_cave = path[-1]
    for next_cave in adj[last_cave]:
        if next_cave == 'start':
            continue
        if next_cave.isupper() or path.count(next_cave) < allowed_small_cave_visits:
            yield path + [next_cave]

def task2(data):
    adj = {}
    for line in data.strip().splitlines():
        a, b = line.split('-')
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return count_pathes_from_start_to_end(adj, extend_path2)


def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
