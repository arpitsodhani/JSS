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


# --- clause: best_score :: (a: list[int]) -> int ---
def best_score(a):
    n = len(a)
    if n == 1:
        return a[0] if a[0] > 0 else 0
    choices = [0, a[0], a[0] + a[1]]
    best = max(choices)
    for i in range(2, n):
        if a[i] > 0:
            best += a[i]
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(best_score(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
