import sys


# --- clause: read_input :: () -> list[tuple[int, str, str]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    cases = []
    at = 1
    for _ in range(t):
        n = int(tokens[at])
        k = int(tokens[at + 1])
        cases.append((k, tokens[at + 2].decode(), tokens[at + 3].decode()))
        at += 4
    return cases


# --- clause: can_change :: (k: int, s: str, t: str) -> bool ---
def can_change(k, s, t):
    n = len(s)
    loose = []
    for i in range(n):
        if i + k < n or i - k >= 0:
            loose.append(i)
        elif s[i] != t[i]:
            return False
    left = sorted(s[i] for i in loose)
    right = sorted(t[i] for i in loose)
    return left == right


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, s, t in read_input():
        out.append("YES" if can_change(k, s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
