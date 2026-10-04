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


# --- clause: can_align :: (a: list[int]) -> bool ---
def can_align(a):
    for head_pos in range(2):
        first = a[head_pos] % 2
        for i in range(head_pos, len(a), 2):
            if a[i] % 2 != first:
                return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_align(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
