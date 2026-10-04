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
    values = list(a)
    rounds = 0
    while True:
        sorted_now = True
        for i in range(n - 1):
            if values[i] > values[i + 1]:
                sorted_now = False
                break
        if sorted_now:
            break
        offset = rounds & 1
        i = offset
        while i + 1 < n:
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
            i += 2
        rounds += 1
    return rounds

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
