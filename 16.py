from __future__ import annotations

import time
from dataclasses import dataclass
from functools import reduce
from typing import List, Optional

import pyperclip


@dataclass
class Literal:
    size: int
    value: int

    @staticmethod
    def from_bits(bits: str, index: int) -> Literal:
        size = 0
        value = 0
        while True:
            value = value * 16 + int(bits[index + size + 1:index + size + 5], 2)
            size += 5
            if bits[index + size - 5] == '0':
                break
        return Literal(size=size, value=value)

@dataclass
class Packet:
    size: int
    version: int
    type_id: int
    literal: Optional[Literal] = None
    subpackets: Optional[List[Packet]] = None

    @staticmethod
    def from_bits(bits: str, index: int) -> Packet:
        version = int(bits[index:index+3], 2)
        type_id = int(bits[index+3:index+6], 2)
        if type_id == 4:
            literal = Literal.from_bits(bits, index + 6)
            size = 6 + literal.size
            return Packet(size=size, version=version, type_id=type_id, literal=literal)
        else:
            length_type_id = int(bits[index+6], 2)
            if length_type_id == 0:
                subpacket_length = int(bits[index+7:index+22], 2)
                size = 22 + subpacket_length
                subpacket_index = index+22
                subpackets = []
                while subpacket_index < index + size:
                    subpackets.append(Packet.from_bits(bits, subpacket_index))
                    subpacket_index += subpackets[-1].size
            else:
                number_of_subpackets = int(bits[index+7:index+18], 2)
                subpacket_index = index+18
                subpackets = []
                for _ in range(number_of_subpackets):
                    subpackets.append(Packet.from_bits(bits, subpacket_index))
                    subpacket_index += subpackets[-1].size
                size = 18 + sum([subpacket.size for subpacket in subpackets])
            return Packet(size=size, version=version, type_id=type_id, subpackets=subpackets)


    def sum_version_numbers(self) -> int:
        result = self.version
        if not self.subpackets:
            return result
        subpackets_result = sum([subpacket.sum_version_numbers() for subpacket in self.subpackets])
        return subpackets_result + result

    def evaluate(self) -> int:
        if self.type_id == 0:
            return sum(map(Packet.evaluate, self.subpackets))
        if self.type_id == 1:
            return reduce(lambda a, b: a * b, map(Packet.evaluate, self.subpackets))
        if self.type_id == 2:
            return min(map(Packet.evaluate, self.subpackets))
        if self.type_id == 3:
            return max(map(Packet.evaluate, self.subpackets))
        if self.type_id == 4:
            return self.literal.value
        if self.type_id == 5:
            return 1 if self.subpackets[0].evaluate() > self.subpackets[1].evaluate() else 0
        if self.type_id == 6:
            return 1 if self.subpackets[0].evaluate() < self.subpackets[1].evaluate() else 0
        if self.type_id == 7:
            return 1 if self.subpackets[0].evaluate() == self.subpackets[1].evaluate() else 0


def parse_data(data):
    bits = []
    for nibble in data.strip():
        nibble_int = int(nibble, 16)
        bits.append('0' if nibble_int & 8 == 0 else '1')
        bits.append('0' if nibble_int & 4 == 0 else '1')
        bits.append('0' if nibble_int & 2 == 0 else '1')
        bits.append('0' if nibble_int & 1 == 0 else '1')
    return ''.join(bits)

def task1(data):
    bits = parse_data(data)
    packet = Packet.from_bits(bits, 0)
    return packet.sum_version_numbers()

def task2(data):
    bits = parse_data(data)
    packet = Packet.from_bits(bits, 0)
    return packet.evaluate()

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
