import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    reader = 1
    cases = []
    for _ in range(t):
        k = int(raw[reader + 1])
        s = raw[reader + 2].decode()
        reader += 3
        cases.append((k, s))
    return cases


# --- clause: can_clear :: (k: int, s: str) -> bool ---
def can_clear(k, s):
    for begin in range(k):
        ones = 0
        for i in range(begin, len(s), k):
            if s[i] == "1":
                ones += 1
        if ones % 2:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, s in read_input():
        out.append("YES" if can_clear(k, s) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
