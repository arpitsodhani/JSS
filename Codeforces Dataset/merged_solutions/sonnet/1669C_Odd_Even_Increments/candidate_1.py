import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: can_align :: (a: list[int]) -> bool ---
def can_align(a):
    for start in range(2):
        first = a[start] % 2
        for i in range(start, len(a), 2):
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
