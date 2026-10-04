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
    total = sum(v for v in a[2:] if v > 0)
    head = 0
    if a[0] > head:
        head = a[0]
    if n > 1 and a[0] + a[1] > head:
        head = a[0] + a[1]
    return total + head


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(best_score(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
