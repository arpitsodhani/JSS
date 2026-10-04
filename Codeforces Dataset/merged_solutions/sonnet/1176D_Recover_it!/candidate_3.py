import sys
from array import array


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return n, fields[1:1 + 2 * n]


# --- clause: sieve_tables :: (limit: int) -> tuple[array, array] ---
def sieve_tables(limit):
    smallest = array('i', [0]) * (limit + 1)
    for element in range(2, limit + 1):
        if smallest[element] == 0:
            jump = element
            while jump <= limit:
                if smallest[jump] == 0:
                    smallest[jump] = element
                jump += element
    rank = array('i', [0]) * (limit + 1)
    seen = 0
    for element in range(2, limit + 1):
        if smallest[element] == element:
            seen += 1
        rank[element] = seen
    return smallest, rank


# --- clause: recover :: (n: int, b: list[int], smallest: array, rank: array) -> list[int] ---
def recover(n, b, smallest, rank):
    top = max(b)
    left = [0] * (top + 1)
    for element in b:
        left[element] += 1
    answer = []
    for element in range(top, 1, -1):
        while left[element]:
            left[element] -= 1
            if smallest[element] == element:
                mate = rank[element]
                answer.append(mate)
            else:
                mate = element // smallest[element]
                answer.append(element)
            left[mate] -= 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, b = read_input()
    smallest, rank = sieve_tables(max(b))
    sys.stdout.write(" ".join(map(str, recover(n, b, smallest, rank))) + "\n")


if __name__ == "__main__":
    main()
