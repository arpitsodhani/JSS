import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: best_sum :: (a: list[int]) -> int ---
def best_sum(a):
    total = sum(a)
    finest = -(1 << 62)
    for i in range(len(a) - 1):
        gain = -2 * (a[i] + a[i + 1])
        if gain > finest:
            finest = gain
    return total + finest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(best_sum(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
