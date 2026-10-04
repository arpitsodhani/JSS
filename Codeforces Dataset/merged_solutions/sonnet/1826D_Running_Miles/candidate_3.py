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


# --- clause: best_jog :: (b: list[int]) -> int ---
def best_jog(b):
    n = len(b)
    ahead = [0] * n
    behind = [0] * n
    ahead[0] = b[0] + 0
    for i in range(1, n):
        here = b[i] + i
        ahead[i] = here if here > ahead[i - 1] else ahead[i - 1]
    behind[n - 1] = b[n - 1] - (n - 1)
    for i in range(n - 2, -1, -1):
        here = b[i] - i
        behind[i] = here if here > behind[i + 1] else behind[i + 1]
    best = -(1 << 62)
    for j in range(1, n - 1):
        summed = ahead[j - 1] + b[j] + behind[j + 1]
        if summed > best:
            best = summed
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for b in read_input():
        out.append(best_jog(b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
