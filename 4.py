import time

import pyperclip


class BingoBoard:
    def __init__(self, board_str):
        self.board = []
        for line in board_str.strip().splitlines():
            self.board.append([])
            for number in line.split():
                self.board[-1].append(int(number))

    def did_win(self, marked):
        for row in self.board + list(zip(*self.board)):
            if set(row).issubset(marked):
                return True
        return False

    def sum_unmarked(self, marked):
        s = 0
        for row in self.board:
            for item in row:
                if item not in marked:
                    s += item
        return s

def parse_data(data):
    numbers, boards = data.split('\n\n', 1)
    numbers = list(map(int, numbers.split(',')))
    boards = list(map(BingoBoard, boards.split('\n\n')))
    return numbers, boards

def task1(data):
    numbers, boards = parse_data(data)
    marked = set()
    for number in numbers:
        marked.add(number)
        for board in boards:
            if board.did_win(marked):
                return board.sum_unmarked(marked) * number

def task2(data):
    numbers, boards = parse_data(data)
    marked = set()
    for number in numbers:
        marked.add(number)
        boards_that_didnt_win = [board for board in boards if not board.did_win(marked)]
        if boards_that_didnt_win == []:
            last_board = boards[0]
            return last_board.sum_unmarked(marked) * number
        boards = boards_that_didnt_win

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    pyperclip.copy(answer)
    print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
