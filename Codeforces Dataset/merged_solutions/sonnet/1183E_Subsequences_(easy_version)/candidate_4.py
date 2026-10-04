import sys


# --- clause: read_input :: () -> tuple[int, int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, data[2].decode()


# --- clause: distinct_counts :: (n: int, s: str) -> list[int] ---
def distinct_counts(n, s):
    rows = [[0] * (n + 1) for _ in range(n + 1)]
    rows[0][0] = 1
    seen = [0] * 26
    for i in range(1, n + 1):
        code = ord(s[i - 1]) - 97
        rows[i][0] = 1
        previous = seen[code]
        for length in range(1, i + 1):
            value = rows[i - 1][length] + rows[i - 1][length - 1]
            if previous:
                value -= rows[previous - 1][length - 1]
            rows[i][length] = value
        seen[code] = i
    return rows[n]


# --- clause: cheapest_set :: (n: int, k: int, s: str) -> int ---
def cheapest_set(n, k, s):
    counts = distinct_counts(n, s)
    need = k
    price = 0
    length = n
    while length >= 0 and need > 0:
        available = counts[length]
        used = available if available < need else need
        price += used * (n - length)
        need -= used
        length -= 1
    if need > 0:
        return -1
    return price

# --- clause: main :: () -> None ---
def main():
    n, k, s = read_input()
    sys.stdout.write(str(cheapest_set(n, k, s)) + "\n")


if __name__ == "__main__":
    main()
