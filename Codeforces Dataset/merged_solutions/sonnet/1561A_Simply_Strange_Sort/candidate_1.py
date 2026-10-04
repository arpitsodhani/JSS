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


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    n = len(a)
    a = list(a)
    rounds = 0
    while True:
        done = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                done = False
                break
        if done:
            return rounds
        start = rounds % 2
        for i in range(start, n - 1, 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        rounds += 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
