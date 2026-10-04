import sys
from array import array


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + 2 * n]


# --- clause: sieve_tables :: (limit: int) -> tuple[array, array] ---
def sieve_tables(limit):
    smallest = array('i', [0]) * (limit + 1)
    for value in range(2, limit + 1):
        if smallest[value] == 0:
            step = value
            while step <= limit:
                if smallest[step] == 0:
                    smallest[step] = value
                step += value
    rank = array('i', [0]) * (limit + 1)
    seen = 0
    for value in range(2, limit + 1):
        if smallest[value] == value:
            seen += 1
        rank[value] = seen
    return smallest, rank


# --- clause: recover :: (n: int, b: list[int], smallest: array, rank: array) -> list[int] ---
def recover(n, b, smallest, rank):
    top = max(b)
    left = [0] * (top + 1)
    for value in b:
        left[value] += 1
    answer = []
    for value in range(top, 1, -1):
        while left[value]:
            left[value] -= 1
            if smallest[value] == value:
                mate = rank[value]
                answer.append(mate)
            else:
                mate = value // smallest[value]
                answer.append(value)
            left[mate] -= 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, b = read_input()
    smallest, rank = sieve_tables(max(b))
    sys.stdout.write(" ".join(map(str, recover(n, b, smallest, rank))) + "\n")


if __name__ == "__main__":
    main()
