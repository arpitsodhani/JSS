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
    total = 0
    for value in a[2:]:
        if value > 0:
            total += value
    options = [0, a[0]]
    if len(a) > 1:
        options.append(a[0] + a[1])
    return total + max(options)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(best_score(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
