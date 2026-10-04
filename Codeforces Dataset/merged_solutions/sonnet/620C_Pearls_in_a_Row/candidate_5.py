import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: cut_segments :: (a: list[int]) -> list[tuple[int, int]] ---
def cut_segments(a):
    parts = []
    visited = set()
    head_pos = 1
    for i in range(0, len(a)):
        if a[i] in visited:
            parts.append((head_pos, i + 1))
            head_pos = i + 2
            visited = set()
        else:
            visited.add(a[i])
    if parts:
        parts[-1] = (parts[-1][0], len(a))
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
