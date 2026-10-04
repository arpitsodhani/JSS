import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    cases = []
    for i in range(t):
        cases.append(tokens[2 + 2 * i].decode())
    return cases


# --- clause: strip_prefixes :: (s: str) -> tuple[int, int] ---
def strip_prefixes(s):
    n = len(s)
    at = 0
    steps = 0
    while at + 1 < n:
        if s[at] == s[at + 1] or s[at] == "(":
            steps += 1
            at += 2
            continue
        j = at + 2
        while j < n and s[j] == "(":
            j += 1
        if j == n:
            break
        steps += 1
        at = j + 1
    return steps, n - at


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        steps, rest = strip_prefixes(s)
        lines.append("%d %d" % (steps, rest))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
