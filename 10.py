import time

import pyperclip


def error_char_completion_suffix(line):
    seen = []
    for c in line:
        if c in '([{<':
            seen.append(c)
        elif c == ')' and seen and seen[-1] == '(':
            seen.pop()
        elif c == ']' and seen and seen[-1] == '[':
            seen.pop()
        elif c == '}' and seen and seen[-1] == '{':
            seen.pop()
        elif c == '>' and seen and seen[-1] == '<':
            seen.pop()
        else:
            return c, []
    return None, seen

def error_char_score(char):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return scores.get(char, 0)

def task1(data):
    lines = data.strip().splitlines()
    error_score = sum(error_char_score(error_char_completion_suffix(l)[0]) for l in lines)
    print(error_score)
    return error_score

def suffix_score(suffix):
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for c in reversed(suffix):
        score = score*5 + scores[c]
    return score

def task2(data):
    lines = data.strip().splitlines()
    completion_suffixes = [error_char_completion_suffix(l)[1] for l in lines]
    relevant_completion_suffixes = [item for item in completion_suffixes if item != []]
    scores = sorted([suffix_score(suffix) for suffix in relevant_completion_suffixes])
    return scores[len(scores) // 2]

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
