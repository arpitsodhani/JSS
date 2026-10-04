import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()


# --- clause: reach_tables :: (a: str, b: str) -> tuple[list[int], list[int]] ---
def reach_tables(a, b):
    n = len(a)
    m = len(b)
    big = n + 1
    prefix = [0] * (m + 1)
    at = 0
    for i in range(m):
        if at < big:
            while at < n and a[at] != b[i]:
                at += 1
            if at == n:
                at = big
            else:
                at += 1
        prefix[i + 1] = at
    suffix = [0] * (m + 2)
    at = 0
    for j in range(m - 1, -1, -1):
        if at < big:
            while at < n and a[n - 1 - at] != b[j]:
                at += 1
            if at == n:
                at = big
            else:
                at += 1
        suffix[j] = at
    suffix[m] = 0
    return prefix, suffix


# --- clause: shortest_cut :: (a: str, b: str) -> str ---
def shortest_cut(a, b):
    n = len(a)
    m = len(b)
    prefix, suffix = reach_tables(a, b)
    best_i = 0
    best_j = m
    best_len = m
    j = 0
    for i in range(m + 1):
        if prefix[i] > n:
            break
        if j < i:
            j = i
        while j <= m and prefix[i] + suffix[j] > n:
            j += 1
        if j > m:
            break
        if j - i < best_len:
            best_len = j - i
            best_i = i
            best_j = j
    answer = b[:best_i] + b[best_j:]
    return answer if answer else "-"


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(shortest_cut(a, b) + "\n")


if __name__ == "__main__":
    main()
