import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: can_sort :: (a: list[int]) -> bool ---
def can_sort(a):
    ranked = sorted(a)
    here = {}
    there = {}
    for i in range(len(a)):
        key = (a[i], i % 2)
        here[key] = here.get(key, 0) + 1
        other = (ranked[i], i % 2)
        there[other] = there.get(other, 0) + 1
    return here == there


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a in read_input():
        pieces.append("YES" if can_sort(a) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
