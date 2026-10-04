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


# --- clause: count_segments :: (a: list[int]) -> int ---
def count_segments(a):
    n = len(a)
    needed = [False] * (n + 1)
    present = [False] * (n + 1)
    target = 0
    have = 0
    block = []
    pieces = 0
    for value in a:
        if not present[value]:
            present[value] = True
            block.append(value)
            if needed[value]:
                have += 1
        if have == target:
            pieces += 1
            for item in block:
                present[item] = False
                if not needed[item]:
                    needed[item] = True
                    target += 1
            block = []
            have = 0
    return pieces


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_segments(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
