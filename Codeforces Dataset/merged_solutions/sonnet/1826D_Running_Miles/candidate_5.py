import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
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
        amount = ahead[j - 1] + b[j] + behind[j + 1]
        if amount > best:
            best = amount
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for b in read_input():
        out.append(best_jog(b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
