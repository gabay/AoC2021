import time

import pyperclip


def task1(data):
    lines = data.strip().splitlines()
    count = 0
    for line in lines:
        result = line.split('|')[1].strip().split()
        for item in result:
            if len(item) in (2, 3, 4, 7):
                count += 1
    return count

def parse_display(entries):
    length_to_segments = {}
    for entry in entries:
        segments = frozenset(entry)
        length_to_segments.setdefault(len(segments), set()).add(segments)

    one_segments = length_to_segments[2].pop()
    four_segments = length_to_segments[4].pop()
    seven_segments = length_to_segments[3].pop()
    eight_segments = length_to_segments[7].pop()
    segments_to_number = {
        one_segments: 1,
        four_segments: 4,
        seven_segments: 7,
        eight_segments: 8,
    }

    for segment in length_to_segments[5]:
        if len(segment & one_segments) == 2:
            segments_to_number[segment] = 3
        elif len(segment & four_segments) == 3:
            segments_to_number[segment] = 5
        else:
            segments_to_number[segment] = 2

    for segment in length_to_segments[6]:
        if len(segment & one_segments) != 2:
            segments_to_number[segment] = 6
        elif len(segment & four_segments) != 4:
            segments_to_number[segment] = 0
        else:
            segments_to_number[segment] = 9

    return segments_to_number

def task2(data):
    lines = data.strip().splitlines()
    result = 0
    for line in lines:
        segments_to_number = parse_display(line.split('|')[0].split())
        line_result = 0
        for entry in line.split('|')[1].split():
            line_result = line_result * 10 + segments_to_number[frozenset(entry)]
        result += line_result
    return result

def main():
    start_time = time.time()
    answer = task2(pyperclip.paste())
    if answer:
        pyperclip.copy(answer)
        print(f'Answer (also in clipboard): {answer}')
    print(f'Time taken: {time.time() - start_time:0.2f}')

if __name__ == '__main__':
    main()
