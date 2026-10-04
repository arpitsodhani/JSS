# CLAUSE: setup_environment
import sys

def parse_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return 0, 0, []
    n, c = values[0], values[1]
    pos = 2
    packed = []
    for _ in range(n):
        size = values[pos]
        pos += 1
        packed.append(tuple(values[pos:pos + size]))
        pos += size
    return n, c, packed

# CLAUSE: solve_logic
def main():
    n, c, words = parse_input()
    if n == 0:
        return
    changes = [0] * (c + 1)

    for left_word, right_word in zip(words, words[1:]):
        found = -1
        for k, pair in enumerate(zip(left_word, right_word)):
            if pair[0] != pair[1]:
                found = k
                break

        if found < 0:
            if len(left_word) > len(right_word):
                print(-1)
                return
            continue

        left_char = left_word[found] - 1
        right_char = right_word[found] - 1

        if left_char < right_char:
            begin = c - right_char
            end = c - left_char
            changes[begin] += 1
            changes[end] -= 1
        else:
            end_first = c - left_char
            begin_second = c - right_char
            changes[0] += 1
            changes[end_first] -= 1
            changes[begin_second] += 1
            changes[c] -= 1

    blocked = 0
    for candidate, delta in enumerate(changes[:-1]):
        blocked += delta
        if blocked == 0:
            print(candidate)
            return
    print(-1)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
