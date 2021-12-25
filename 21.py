from __future__ import annotations

import itertools
import re
import time

import pyperclip


def d100_deterministic_cube(n = 100):
    for i in itertools.count(2, 3):
        yield ((i - 1) % n) + 1

def move(p, roll) -> int:
    new_p = (p + roll) % 10
    if new_p == 0:
        new_p = 10
    return new_p

def game1(p1, p2):
    s1, s2 = 0, 0
    for i, roll in enumerate(d100_deterministic_cube(), 1):
        if i % 2 == 1:
            p1 = move(p1, roll * 3)
            s1 += p1
            if s1 >= 1000:
                return s2, i * 3
        else:
            p2 = move(p2, roll * 3)
            s2 += p2
            if s2 >= 1000:
                return s1, i * 3

def task1(data):
    p1, p2 = map(int, re.findall(r': (\d)', data))
    losing_score, rolls = game1(p1, p2)
    print(losing_score, rolls)
    return losing_score * rolls


def d3_multidimentional_cube():
    for i, j, k in itertools.product(range(1, 4), range(1, 4), range(1, 4)):
        yield i + j + k

def game2_turn(games_per_state, s1, s2, p1, p2, is_p1_turn):
    games = games_per_state.get((s1, s2, p1, p2, is_p1_turn), 0)
    if not games:
        return
    for roll_sum in d3_multidimentional_cube():
        if is_p1_turn:
            new_p1 = move(p1, roll_sum)
            new_s1 = s1 + new_p1
            state = (new_s1, s2, new_p1, p2, not is_p1_turn)
        else:
            new_p2 = move(p2, roll_sum)
            new_s2 = s2 + new_p2
            state = (s1, new_s2, p1, new_p2, not is_p1_turn)
        if state not in games_per_state:
            games_per_state[state] = games
        else:
            games_per_state[state] += games




def game2(p1, p2):
    games_per_state = {(0, 0, p1, p2, True): 1}
    for s1, s2 in itertools.product(range(21), range(21)):
        for p1, p2 in itertools.product(range(1, 11), range(1, 11)):
            game2_turn(games_per_state, s1, s2, p1, p2, True)
            game2_turn(games_per_state, s1, s2, p1, p2, False)
    p1_wins = 0
    p2_wins = 0
    for state, games in games_per_state.items():
        if state[0] >= 21:
            p1_wins += games
        elif state[1] >= 21:
            p2_wins += games
    return p1_wins, p2_wins

def task2(data):
    p1, p2 = map(int, re.findall(r': (\d)', data))
    p1_wins, p2_wins = game2(p1, p2)
    print(p1_wins, p2_wins)
    return max(p1_wins, p2_wins)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
