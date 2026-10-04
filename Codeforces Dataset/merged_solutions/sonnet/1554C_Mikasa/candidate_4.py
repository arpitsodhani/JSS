import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: smallest_missing :: (n: int, m: int) -> int ---
def smallest_missing(n, m):
    target = m + 1
    mine = []
    value = n
    while value:
        mine.append(value & 1)
        value >>= 1
    theirs = []
    value = target
    while value:
        theirs.append(value & 1)
        value >>= 1
    while len(mine) < len(theirs):
        mine.append(0)
    while len(theirs) < len(mine):
        theirs.append(0)
    answer = 0
    for bit in range(len(theirs) - 1, -1, -1):
        if mine[bit] == theirs[bit]:
            continue
        if theirs[bit]:
            answer += 1 << bit
        else:
            break
    return answer


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(smallest_missing(n, m))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
