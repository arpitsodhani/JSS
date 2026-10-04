import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append(list(map(int, data[pos:pos + n])))
        pos += n
    return cases


# --- clause: can_sort :: (values: list[int]) -> str ---
def can_sort(values):
    total = len(values)
    i = 1
    while i < total:
        if not values[i - 1] > values[i]:
            return "YES"
        i += 1
    return "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(can_sort(values))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
