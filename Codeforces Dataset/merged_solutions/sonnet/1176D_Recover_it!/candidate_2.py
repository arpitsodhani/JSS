import sys
from array import array


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return n, tokens[1:1 + 2 * n]


# --- clause: sieve_tables :: (limit: int) -> tuple[array, array] ---
def sieve_tables(limit):
    smallest = array('i', [0]) * (limit + 1)
    for item in range(2, limit + 1):
        if smallest[item] == 0:
            step = item
            while step <= limit:
                if smallest[step] == 0:
                    smallest[step] = item
                step += item
    rank = array('i', [0]) * (limit + 1)
    seen = 0
    for item in range(2, limit + 1):
        if smallest[item] == item:
            seen += 1
        rank[item] = seen
    return smallest, rank


# --- clause: recover :: (n: int, b: list[int], smallest: array, rank: array) -> list[int] ---
def recover(n, b, smallest, rank):
    top = max(b)
    left = [0] * (top + 1)
    for item in b:
        left[item] += 1
    answer = []
    for item in range(top, 1, -1):
        while left[item]:
            left[item] -= 1
            if smallest[item] == item:
                mate = rank[item]
                answer.append(mate)
            else:
                mate = item // smallest[item]
                answer.append(item)
            left[mate] -= 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, b = read_input()
    smallest, rank = sieve_tables(max(b))
    sys.stdout.write(" ".join(map(str, recover(n, b, smallest, rank))) + "\n")


if __name__ == "__main__":
    main()
