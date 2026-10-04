import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    cur = list(a)
    best = sum(cur)
    while len(cur) > 1:
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        total = sum(cur)
        if total < 0:
            total = -total
        if total > best:
            best = total
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
