import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: split_points :: (a: list[int]) -> list[int] ---
def split_points(a):
    n = len(a)
    cursor = [False] * (n + 1)
    seen = set()
    top = 0
    for i in range(n):
        seen.add(a[i])
        if a[i] > top:
            top = a[i]
        if top == i + 1 and len(seen) == i + 1:
            cursor[i + 1] = True
    tail = [False] * (n + 2)
    seen = set()
    top = 0
    for i in range(n - 1, -1, -1):
        seen.add(a[i])
        if a[i] > top:
            top = a[i]
        if top == n - i and len(seen) == n - i:
            tail[i] = True
    cuts = []
    for cut in range(1, n):
        if cursor[cut] and tail[cut]:
            cuts.append(cut)
    return cuts


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        cuts = split_points(a)
        out.append(str(len(cuts)))
        for cut in cuts:
            out.append("%d %d" % (cut, len(a) - cut))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
