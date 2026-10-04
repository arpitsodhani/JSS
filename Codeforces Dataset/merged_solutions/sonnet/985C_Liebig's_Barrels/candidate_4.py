import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    k = values[1]
    l = values[2]
    arr = sorted(values[3:3 + n * k])
    return n, k, l, arr


# --- clause: count_usable :: (staves: list[int], l: int) -> int ---
def count_usable(staves, l):
    threshold = staves[0] + l
    usable = len(staves)
    for i in range(len(staves)):
        if staves[i] > threshold:
            usable = i
            break
    return usable


# --- clause: compute_answer :: (n: int, k: int, staves: list[int], usable: int) -> int ---
def compute_answer(n, k, staves, usable):
    if usable < n:
        return 0
    answer = 0
    at = 0
    for done in range(n):
        answer += staves[at]
        rest = n - done - 1
        at += min(k, usable - at - rest)
    return answer


# --- clause: main :: () -> None ---
def main():
    params = read_input()
    usable = count_usable(params[3], params[2])
    print(compute_answer(params[0], params[1], params[3], usable))


if __name__ == "__main__":
    main()
