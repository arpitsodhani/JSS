import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    q = fields[0]
    cursor = 1
    cases = []
    for _ in range(q):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: biggest_gift :: (a: list[int]) -> int ---
def biggest_gift(a):
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    sizes = sorted(tally.values(), reverse=True)
    running = 0
    allowed = len(a) + 1
    for size in sizes:
        take = size if size < allowed - 1 else allowed - 1
        if take <= 0:
            break
        running += take
        allowed = take
    return running


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(biggest_gift(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
