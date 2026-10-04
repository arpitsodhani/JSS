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


# --- clause: good_order :: (a: list[int]) -> list[int] ---
def good_order(a):
    return sorted(a, reverse=True)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, good_order(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
