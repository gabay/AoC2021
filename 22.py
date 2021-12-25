import itertools
import re
import time
from dataclasses import dataclass
from typing import List, Optional

import pyperclip


@dataclass
class Zone:
    x: range
    y: range
    z: range
    removed_zones: List["Zone"]

    def size(self) -> int:
        # return len(self.x) * len(self.y) * len(self.z)
        return len(self.x) * len(self.y) * len(self.z) - sum([z.size() for z in self.removed_zones])

    def remove(self, zone: "Zone"):
        intersection = self.intersect(zone)
        if intersection:
            for z in self.removed_zones:
                z.remove(intersection)
            self.removed_zones.append(intersection)

    def intersect(self, other: "Zone") -> Optional["Zone"]:
        x = intersect(self.x, other.x)
        y = intersect(self.y, other.y)
        z = intersect(self.z, other.z)
        if not x or not y or not z:
            return None
        return Zone(x, y, z, [])

def intersect(a: range, b: range) -> Optional[range]:
    if a.stop <= b.start or b.stop <= a.start:
        return None

    return range(max(a.start, b.start), min(a.stop, b.stop))

@dataclass
class Action:
    on: bool
    zone: Zone

def parse_data(data):
    for line in data.splitlines():
        on = line.startswith("on ")
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"\-?\d+", line))
        zone = Zone(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1), [])
        yield Action(on, zone)

def is_on(actions, x, y, z):
    for action in reversed(actions):
        if action.has_point(x, y, z):
            return action.on
    return False

def task1(data):
    actions = list(parse_data(data))
    on = 0
    for x, y, z in itertools.product(range(-50, 51), range(-50, 51), range(-50, 51)):
        if is_on(actions, x, y, z):
            on += 1
    return on

def task2(data):
    actions = parse_data(data)
    zones: List[Zone] = []
    for action in actions:
        for zone in zones:
            zone.remove(action.zone)
        if action.on:
            zones.append(action.zone)
    return sum([zone.size() for zone in zones])

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
