import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k


# --- clause: lucky_numbers :: (limit: int) -> list[int] ---
def lucky_numbers(limit):
    found = []
    frontier = [4, 7]
    while frontier:
        nxt = []
        for value in frontier:
            if value <= limit:
                found.append(value)
                nxt.append(value * 10 + 4)
                nxt.append(value * 10 + 7)
        frontier = nxt
    return found


# --- clause: count_matches :: (n: int, k: int) -> int ---
def count_matches(n, k):
    factorial = [1]
    while factorial[-1] < k and len(factorial) <= 20:
        factorial.append(factorial[-1] * len(factorial))
    tail = 0
    while factorial[tail] < k:
        tail += 1
    if tail > n:
        return -1
    fixed = n - tail
    lucky = lucky_numbers(n)
    total = 0
    for value in lucky:
        if value <= fixed:
            total += 1
    pool = list(range(fixed + 1, n + 1))
    rank = k - 1
    order = []
    for slot in range(tail, 0, -1):
        block = factorial[slot - 1]
        pick = rank // block
        rank -= pick * block
        order.append(pool.pop(pick))
    lucky_set = set(lucky)
    for offset in range(tail):
        position = fixed + 1 + offset
        if position in lucky_set and order[offset] in lucky_set:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write(str(count_matches(n, k)) + "\n")


if __name__ == "__main__":
    main()
