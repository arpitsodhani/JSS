import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    l = data[2]
    staves = sorted(data[3:3 + n * k])
    return n, k, l, staves


# --- clause: count_usable :: (staves: list[int], l: int) -> int ---
def count_usable(staves, l):
    limit = staves[0] + l
    usable = 0
    for v in staves:
        if v > limit:
            break
        usable += 1
    return usable


# --- clause: compute_answer :: (n: int, k: int, staves: list[int], usable: int) -> int ---
def compute_answer(n, k, staves, usable):
    if usable < n:
        return 0
    ans = 0
    pos = 0
    for barrel in range(n):
        ans += staves[pos]
        remaining = n - barrel - 1
        pos += min(k, usable - pos - remaining)
    return ans


# --- clause: main :: () -> None ---
def main():
    n, k, l, staves = read_input()
    usable = count_usable(staves, l)
    print(compute_answer(n, k, staves, usable))


if __name__ == "__main__":
    main()
