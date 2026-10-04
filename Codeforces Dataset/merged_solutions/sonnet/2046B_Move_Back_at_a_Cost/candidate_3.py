import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: smallest_array :: (a: list[int]) -> list[int] ---
def smallest_array(a):
    n = len(a)
    suffix = [0] * (n + 1)
    suffix[n] = 10 ** 18
    for i in range(n - 1, -1, -1):
        suffix[i] = a[i] if a[i] < suffix[i + 1] else suffix[i + 1]
    kept = []
    moved = []
    for i in range(n):
        if a[i] > suffix[i + 1]:
            moved.append(a[i] + 1)
        else:
            kept.append(a[i])
    if not moved:
        return kept
    moved.sort()
    ceiling = moved[0]
    front = []
    for i in range(len(kept)):
        if kept[i] > ceiling:
            moved.append(kept[i] + 1)
        else:
            front.append(kept[i])
    moved.sort()
    return front + moved


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, smallest_array(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
