import re
import time
from collections import Counter

import pyperclip


def parse_rules(raw_rules):
    rules = {}
    for raw_rule in raw_rules.splitlines():
        pattern, result = raw_rule.split(' -> ')
        rules[tuple(pattern)] = result
    return rules

def parse_data(data):
    polymer, raw_rules = data.split('\n\n')
    return polymer, parse_rules(raw_rules)

def extend_polymer(polymer, rules):
    new_polymer = [polymer[0]]
    for pair in zip(polymer[:-1], polymer[1:]):
        extension = rules.get(pair, '')
        new_polymer.append(extension + pair[1])
    return ''.join(new_polymer)

def subtract_least_common_from_most_common(polymer_counter: Counter):
    items = polymer_counter.most_common()
    return items[0][1] - items[-1][1]

def task1(data):
    polymer, rules = parse_data(data)
    for _ in range(10):
        polymer = extend_polymer(polymer, rules)
    return subtract_least_common_from_most_common(Counter(polymer))

def extend_polymer_counter(polymer_counter: Counter, rules):
    new_counter = polymer_counter.copy()
    for pair, count in polymer_counter.items():
        c = rules.get(pair, None)
        if c:
            new_counter[pair] -= count
            new_counter[(pair[0], c)] += count
            new_counter[(c, pair[1])] += count
    return new_counter

def task2(data):
    polymer, rules = parse_data(data)
    polymer_counter = Counter(zip(polymer[:-1], polymer[1:]))
    for i in range(40):
        print(i)
        polymer_counter = extend_polymer_counter(polymer_counter, rules)
    twice_element_count = Counter([polymer[0], polymer[-1]])
    for pair, count in polymer_counter.items():
        twice_element_count[pair[0]] += count
        twice_element_count[pair[1]] += count


    return subtract_least_common_from_most_common(twice_element_count) // 2

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
