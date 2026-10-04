import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: is_shuffle :: (a: list[int]) -> bool ---
def is_shuffle(a):
    n = len(a)
    seen = [False] * n
    for k in range(n):
        spot = (k + a[k]) % n
        if seen[spot]:
            return False
        seen[spot] = True
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if is_shuffle(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
