# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_masks(k):
    masks = []

    def choose(start, left, current):
        if left == 0:
            masks.append(current)
            return
        stop = 15 - left
        for bit in range(start, stop):
            choose(bit + 1, left - 1, current | (1 << bit))

    choose(0, k, 0)
    return masks

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    numbers = data[2:2 + n]
    size = 16384

    if k > 14:
        print(0)
        return

    freq = [0 for _ in range(size)]
    for number in numbers:
        freq[number] = freq[number] + 1

    if k == 0:
        answer = 0
        for count in freq:
            if count > 1:
                answer += count * (count - 1) // 2
        print(answer)
        return

    answer = 0
    masks = build_masks(k)
    for number in range(size):
        count = freq[number]
        if count == 0:
            continue
        for mask in masks:
            other = number ^ mask
            if other > number:
                answer += count * freq[other]

    print(answer)

# CLAUSE: finish_program
main()
