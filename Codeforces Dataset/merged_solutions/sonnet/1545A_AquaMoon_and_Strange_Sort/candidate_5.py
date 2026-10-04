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


# --- clause: can_sort :: (a: list[int]) -> bool ---
def can_sort(a):
    ranked = sorted(a)
    here = {}
    there = {}
    for i in range(0, len(a)):
        key = (a[i], i % 2)
        here[key] = here.get(key, 0) + 1
        other = (ranked[i], i % 2)
        there[other] = there.get(other, 0) + 1
    return here == there


# --- clause: main :: () -> None ---
def main():
    lines = []
    for a in read_input():
        lines.append("YES" if can_sort(a) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
