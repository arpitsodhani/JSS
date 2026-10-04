import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, l = data[0], data[1], data[2]
    lengths = data[3:3 + n * k]
    lengths.sort()
    return n, k, l, lengths


# --- clause: count_usable :: (staves: list[int], l: int) -> int ---
def count_usable(staves, l):
    bound = staves[0] + l
    good = 0
    for value in staves:
        if value > bound:
            break
        good = good + 1
    return good


# --- clause: compute_answer :: (n: int, k: int, staves: list[int], usable: int) -> int ---
def compute_answer(n, k, staves, usable):
    if usable < n:
        return 0
    total = 0
    cursor = 0
    for made in range(n):
        total += staves[cursor]
        left = n - made - 1
        cursor += min(k, usable - cursor - left)
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, l, lengths = read_input()
    good = count_usable(lengths, l)
    sys.stdout.write(str(compute_answer(n, k, lengths, good)) + "\n")


if __name__ == "__main__":
    main()
