import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    values = [int(token) for token in data[2:2 + n]]
    asks = [int(token) for token in data[2 + n:2 + n + q]]
    return n, q, values, asks


# --- clause: warm_up :: (n: int, values: list[int]) -> tuple[list[tuple[int, int]], list[int], int] ---
def warm_up(n, values):
    biggest = max(values)
    line = list(values)
    early = []
    while line[0] != biggest:
        a = line[0]
        b = line[1]
        early.append((a, b))
        line = line[2:]
        if a > b:
            line.insert(0, a)
            line.append(b)
        else:
            line.insert(0, b)
            line.append(a)
    rest = line[1:]
    return early, rest, biggest


# --- clause: answer_query :: (m: int, early: list, rest: list[int], biggest: int) -> str ---
def answer_query(m, early, rest, biggest):
    if m <= len(early):
        a, b = early[m - 1]
        return "%d %d" % (a, b)
    step = (m - len(early) - 1) % len(rest)
    return "%d %d" % (biggest, rest[step])


# --- clause: main :: () -> None ---
def main():
    n, q, values, asks = read_input()
    early, rest, biggest = warm_up(n, values)
    out = []
    for m in asks:
        out.append(answer_query(m, early, rest, biggest))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
