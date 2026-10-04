import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    q = raw[0]
    offset = 1
    cases = []
    for _ in range(q):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: biggest_gift :: (a: list[int]) -> int ---
def biggest_gift(a):
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    sizes = sorted(tally.values(), reverse=True)
    summed = 0
    allowed = len(a) + 1
    for size in sizes:
        take = size if size < allowed - 1 else allowed - 1
        if take <= 0:
            break
        summed += take
        allowed = take
    return summed


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(biggest_gift(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
