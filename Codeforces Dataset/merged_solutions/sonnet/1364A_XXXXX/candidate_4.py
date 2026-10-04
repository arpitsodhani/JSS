import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        x = numbers[cursor + 1]
        cursor += 2
        cases.append((x, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: longest_piece :: (x: int, a: list[int]) -> int ---
def longest_piece(x, a):
    n = len(a)
    if sum(a) % x:
        return n
    first = -1
    last = -1
    for i in range(n):
        if a[i] % x:
            if first < 0:
                first = i
            last = i
    if first < 0:
        return -1
    tail = n - first - 1
    return tail if tail > last else last


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, a in read_input():
        out.append(longest_piece(x, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
