import sys
from array import array


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return n, raw[1:1 + 2 * n]


# --- clause: sieve_tables :: (limit: int) -> tuple[array, array] ---
def sieve_tables(limit):
    smallest = array('i', [0]) * (limit + 1)
    for number in range(2, limit + 1):
        if smallest[number] == 0:
            stride = number
            while stride <= limit:
                if smallest[stride] == 0:
                    smallest[stride] = number
                stride += number
    rank = array('i', [0]) * (limit + 1)
    seen = 0
    for number in range(2, limit + 1):
        if smallest[number] == number:
            seen += 1
        rank[number] = seen
    return smallest, rank


# --- clause: recover :: (n: int, b: list[int], smallest: array, rank: array) -> list[int] ---
def recover(n, b, smallest, rank):
    top = max(b)
    left = [0] * (top + 1)
    for number in b:
        left[number] += 1
    answer = []
    for number in range(top, 1, -1):
        while left[number]:
            left[number] -= 1
            if smallest[number] == number:
                mate = rank[number]
                answer.append(mate)
            else:
                mate = number // smallest[number]
                answer.append(number)
            left[mate] -= 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, b = read_input()
    smallest, rank = sieve_tables(max(b))
    sys.stdout.write(" ".join(map(str, recover(n, b, smallest, rank))) + "\n")


if __name__ == "__main__":
    main()
