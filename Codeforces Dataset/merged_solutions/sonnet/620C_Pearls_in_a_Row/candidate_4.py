import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: cut_segments :: (a: list[int]) -> list[tuple[int, int]] ---
def cut_segments(a):
    parts = []
    seen = {}
    start = 1
    at = 0
    while at < len(a):
        if seen.get(a[at], 0):
            parts.append((start, at + 1))
            start = at + 2
            seen = {}
        else:
            seen[a[at]] = 1
        at += 1
    if len(parts):
        last = parts.pop()
        parts.append((last[0], len(a)))
    return parts


# --- clause: main :: () -> None ---
def main():
    parts = cut_segments(read_input())
    if not parts:
        sys.stdout.write("-1\n")
    else:
        out = [str(len(parts))]
        for left, right in parts:
            out.append("%d %d" % (left, right))
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
