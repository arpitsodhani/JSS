import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    pos = 1
    cases = []
    for _ in range(q):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: biggest_gift :: (a: list[int]) -> int ---
def biggest_gift(a):
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    sizes = sorted(tally.values(), reverse=True)
    total = 0
    allowed = len(a) + 1
    for size in sizes:
        take = size if size < allowed - 1 else allowed - 1
        if take <= 0:
            break
        total += take
        allowed = take
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(biggest_gift(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
