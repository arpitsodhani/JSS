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
    work = list(a)
    rounds = 0
    while True:
        if all(work[i] < work[i + 1] for i in range(n - 1)):
            return rounds
        for i in range(rounds % 2, n - 1, 2):
            if work[i] > work[i + 1]:
                work[i], work[i + 1] = work[i + 1], work[i]
        rounds += 1

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
