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


# --- clause: good_order :: (a: list[int]) -> list[int] ---
def good_order(a):
    return sorted(a, reverse=True)


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a in read_input():
        pieces.append(" ".join(map(str, good_order(a))))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
