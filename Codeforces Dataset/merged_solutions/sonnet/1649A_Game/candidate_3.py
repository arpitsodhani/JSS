import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: jump_cost :: (a: list[int]) -> int ---
def jump_cost(a):
    n = len(a)
    first_gap = -1
    last_gap = -1
    for i in range(n):
        if a[i] == 0:
            if first_gap < 0:
                first_gap = i
            last_gap = i
    if first_gap < 0:
        return 0
    return last_gap - first_gap + 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(jump_cost(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
