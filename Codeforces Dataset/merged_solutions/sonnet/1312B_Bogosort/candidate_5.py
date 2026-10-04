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


# --- clause: good_order :: (a: list[int]) -> list[int] ---
def good_order(a):
    return sorted(a, reverse=True)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for a in read_input():
        lines.append(" ".join(map(str, good_order(a))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
