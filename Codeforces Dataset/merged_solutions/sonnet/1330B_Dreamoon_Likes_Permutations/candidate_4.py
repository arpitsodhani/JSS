import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = numbers[pos]
        pos += 1
        cases.append(numbers[pos:pos + n])
        pos += n
    return cases


# --- clause: split_points :: (a: list[int]) -> list[int] ---
def split_points(a):
    n = len(a)
    head = [False] * (n + 1)
    seen = [False] * (n + 2)
    top = 0
    fine = True
    for i in range(n):
        value = a[i]
        if value > n or seen[value]:
            fine = False
        else:
            seen[value] = True
            if value > top:
                top = value
        if fine and top == i + 1:
            head[i + 1] = True
    tail = [False] * (n + 2)
    seen = [False] * (n + 2)
    top = 0
    fine = True
    for i in range(n - 1, -1, -1):
        value = a[i]
        if value > n or seen[value]:
            fine = False
        else:
            seen[value] = True
            if value > top:
                top = value
        if fine and top == n - i:
            tail[i] = True
    cuts = []
    cut = 1
    while cut < n:
        if head[cut] and tail[cut]:
            cuts.append(cut)
        cut += 1
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
