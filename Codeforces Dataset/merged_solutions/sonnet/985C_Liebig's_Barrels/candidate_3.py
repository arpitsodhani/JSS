import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    spread = tokens[2]
    staves = sorted(tokens[3:3 + n * k])
    return n, k, spread, staves


# --- clause: count_usable :: (staves: list[int], l: int) -> int ---
def count_usable(staves, l):
    ceiling = staves[0] + l
    usable = 0
    for i in range(len(staves)):
        if staves[i] > ceiling:
            break
        usable += 1
    return usable


# --- clause: compute_answer :: (n: int, k: int, staves: list[int], usable: int) -> int ---
def compute_answer(n, k, staves, usable):
    if usable < n:
        return 0
    volume = 0
    index = 0
    for barrel in range(n):
        volume += staves[index]
        still_needed = n - barrel - 1
        take = usable - index - still_needed
        index += take if take < k else k
    return volume


# --- clause: main :: () -> None ---
def main():
    n, k, spread, staves = read_input()
    usable = count_usable(staves, spread)
    answer = compute_answer(n, k, staves, usable)
    print(answer)


if __name__ == "__main__":
    main()
