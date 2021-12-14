import time

import pyperclip


def locations_around(x, y):
    return [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]

class Octopus:
    def __init__(self, level):
        self.level = level

    def step(self):
        self.level += 1

    def receive_nearby_flash(self):
        if not self.did_flash():
            self.step()

    def should_flash(self):
        return self.level > 9

    def did_flash(self):
        return self.level == 0

    def flash(self):
        assert(self.should_flash())
        self.level = 0


class OctopusMap:
    def __init__(self, levels):
        self.octopuses = [[Octopus(level) for level in row] for row in levels]
        self.x = len(self.octopuses[0])
        self.y = len(self.octopuses)

    def step(self):
        [[octopus.step() for octopus in row] for row in self.octopuses]

        for y in range(self.y):
            for x in range(self.x):
                if self.at(x, y).should_flash():
                    self.flash_at(x, y)

        flashes = sum(octopus.did_flash() for octopus in sum(self.octopuses, []))
        return flashes

    def flash_at(self, x, y):
        self.at(x, y).flash()
        for xx, yy in locations_around(x, y):
            if self.has(xx, yy):
                self.at(xx, yy).receive_nearby_flash()
                if self.at(xx, yy).should_flash():
                    self.flash_at(xx, yy)

    def has(self, x, y):
        return 0 <= x < self.x and 0 <= y < self.y

    def at(self, x, y):
        return self.octopuses[y][x]

def count_flashes(octopus_map, rounds):
    flashes = 0
    for _ in range(rounds):
        flashes += octopus_map.step()
    return flashes

def task1(data):
    levels = [[int(level) for level in line] for line in data.strip().splitlines()]
    octopus_map = OctopusMap(levels)
    return count_flashes(octopus_map, 100)

def first_step_where_all_octopuses_flash(octopus_map):
    step = 0
    while True:
        step += 1
        flashes = octopus_map.step()
        if flashes == octopus_map.x * octopus_map.y:
            return step

def task2(data):
    levels = [[int(level) for level in line] for line in data.strip().splitlines()]
    octopus_map = OctopusMap(levels)
    return first_step_where_all_octopuses_flash(octopus_map)

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
