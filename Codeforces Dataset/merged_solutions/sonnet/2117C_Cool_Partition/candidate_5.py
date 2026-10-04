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
    wanted = 0
    outstanding = 0
    collected = []
    pieces = 0
    index = 0
    while index < len(a):
        value = a[index]
        index += 1
        if not present[value]:
            present[value] = True
            collected.append(value)
            if needed[value]:
                outstanding -= 1
        if outstanding == 0:
            pieces += 1
            for item in collected:
                present[item] = False
                if not needed[item]:
                    needed[item] = True
                    wanted += 1
            collected = []
            outstanding = wanted
    return pieces


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_segments(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
