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
    used = 0
    for i in range(m):
        if used <= n:
            step = used
            while step < n and a[step] != b[i]:
                step += 1
            used = big if step == n else step + 1
        prefix[i + 1] = used
    suffix = [0] * (m + 2)
    used = 0
    for j in range(m - 1, -1, -1):
        if used <= n:
            step = used
            while step < n and a[n - 1 - step] != b[j]:
                step += 1
            used = big if step == n else step + 1
        suffix[j] = used
    suffix[m] = 0
    return prefix, suffix


# --- clause: shortest_cut :: (a: str, b: str) -> str ---
def shortest_cut(a, b):
    n = len(a)
    m = len(b)
    prefix, suffix = reach_tables(a, b)
    best_len = m + 1
    best_i = 0
    best_j = m
    for i in range(m + 1):
        if prefix[i] > n:
            break
        lo = i
        hi = m
        while lo < hi:
            mid = (lo + hi) // 2
            if prefix[i] + suffix[mid] <= n:
                hi = mid
            else:
                lo = mid + 1
        if prefix[i] + suffix[lo] <= n and lo - i < best_len:
            best_len = lo - i
            best_i = i
            best_j = lo
    answer = b[:best_i] + b[best_j:]
    return answer if answer else "-"

# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(shortest_cut(a, b) + "\n")


if __name__ == "__main__":
    main()
