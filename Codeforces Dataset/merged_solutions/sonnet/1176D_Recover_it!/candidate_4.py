import sys
from array import array


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return n, numbers[1:1 + 2 * n]


# --- clause: sieve_tables :: (limit: int) -> tuple[array, array] ---
def sieve_tables(limit):
    smallest = array('i', [0]) * (limit + 1)
    for entry in range(2, limit + 1):
        if smallest[entry] == 0:
            step = entry
            while step <= limit:
                if smallest[step] == 0:
                    smallest[step] = entry
                step += entry
    rank = array('i', [0]) * (limit + 1)
    seen = 0
    for entry in range(2, limit + 1):
        if smallest[entry] == entry:
            seen += 1
        rank[entry] = seen
    return smallest, rank


# --- clause: recover :: (n: int, b: list[int], smallest: array, rank: array) -> list[int] ---
def recover(n, b, smallest, rank):
    top = max(b)
    left = [0 for _ in range(top + 1)]
    for entry in b:
        left[entry] += 1
    answer = []
    for entry in range(top, 1, -1):
        while left[entry]:
            left[entry] -= 1
            if smallest[entry] == entry:
                mate = rank[entry]
                answer.append(mate)
            else:
                mate = entry // smallest[entry]
                answer.append(entry)
            left[mate] -= 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, b = read_input()
    smallest, rank = sieve_tables(max(b))
    sys.stdout.write(" ".join(map(str, recover(n, b, smallest, rank))) + "\n")


if __name__ == "__main__":
    main()
