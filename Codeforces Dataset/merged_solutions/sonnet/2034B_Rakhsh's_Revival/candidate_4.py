import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        m = int(data[pos + 1])
        k = int(data[pos + 2])
        s = data[pos + 3]
        pos += 4
        cases.append((n, m, k, s))
    return cases


# --- clause: timar_uses :: (n: int, m: int, k: int, s: bytes) -> int ---
def timar_uses(n, m, k, s):
    used = 0
    run = 0
    i = 0
    while i < n:
        if s[i] == 48:
            run += 1
            if run == m:
                used += 1
                i += k
                run = 0
                continue
        else:
            run = 0
        i = i + 1
    return used


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(timar_uses(case[0], case[1], case[2], case[3])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
