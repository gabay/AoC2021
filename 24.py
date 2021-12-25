from __future__ import annotations

import time
from dataclasses import dataclass
from typing import List

import pyperclip


@dataclass
class ALU:
    input: List[int]
    w: int = 0
    x: int = 0
    y: int = 0
    z: int = 0

    def process(self, command: str):
        cmd, *args = command.split()
        getattr(self, cmd)(*args)
        # print(command, '\t', self)

    def inp(self, a: str):
        self._set(a, self.input[0])
        self.input = self.input[1:]

    def add(self, a: str, b: str):
        result = self._get(a) + self._get(b)
        self._set(a, result)

    def mul(self, a: str, b: str):
        result = self._get(a) * self._get(b)
        self._set(a, result)

    def div(self, a: str, b: str):
        result = int(self._get(a) / self._get(b))
        self._set(a, result)

    def mod(self, a: str, b: str):
        result = self._get(a) % self._get(b)
        self._set(a, result)

    def eql(self, a: str, b: str):
        if a == 'x' and b == 'w':
            print("EQL", self.x, self.w)
        result = 1 if self._get(a) == self._get(b) else 0
        self._set(a, result)

    def _get(self, a: str):
        if a in 'wxyz':
            return getattr(self, a)
        else:
            return int(a)

    def _set(self, a: str, v: int):
        assert a in 'wxyz'
        return setattr(self, a, v)

def process(input: List[int], commands: List[str]) -> ALU:
    alu = ALU(input)
    for command in commands:
        alu.process(command)
    return alu

def get_highest_input():
    return [9,4,9,9,2,9,9,4,1,9,5,9,9,8]

def get_lowest_input():
    return [2,1,1,9,1,8,6,1,1,5,1,1,6,1]

def task1(data):
    commands = data.splitlines()
    inp = get_highest_input()
    alu = process(inp, commands)
    print(inp, alu)
    return int(''.join(map(str, inp)))

def task2(data):
    commands = data.splitlines()
    inp = get_lowest_input()
    alu = process(inp, commands)
    print(inp, alu)
    return int(''.join(map(str, inp)))

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
