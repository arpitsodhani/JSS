# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0

    n = numbers[pos]
    pos += 1

    frequency = defaultdict(int)
    for _ in range(n):
        frequency[numbers[pos]] += 1
        pos += 1

    m = numbers[pos]
    pos += 1

    audio_start = pos
    subtitle_start = pos + m

    best_index = 0
    best_pair = (-1, -1)

    for index, language in enumerate(numbers[audio_start:audio_start + m]):
        pair = (frequency[language], frequency[numbers[subtitle_start + index]])
        if pair > best_pair:
            best_pair = pair
            best_index = index

    sys.stdout.write(str(best_index + 1))

# CLAUSE: finish_program
main()
