import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    q = int(data[1])
    values = [int(token) for token in data[2:2 + n]]
    asks = [int(data[2 + n + i]) for i in range(q)]
    return n, q, values, asks


# --- clause: warm_up :: (n: int, values: list[int]) -> tuple[list[tuple[int, int]], list[int], int] ---
def warm_up(n, values):
    biggest = values[0]
    for value in values:
        if value > biggest:
            biggest = value
    line = list(values)
    head = 0
    early = []
    while line[head] != biggest:
        a = line[head]
        b = line[head + 1]
        head += 1
        early.append((a, b))
        if a > b:
            line[head] = a
            line.append(b)
        else:
            line.append(a)
    rest = line[head + 1:]
    return early, rest, biggest


# --- clause: answer_query :: (m: int, early: list, rest: list[int], biggest: int) -> str ---
def answer_query(m, early, rest, biggest):
    if m <= len(early):
        pair = early[m - 1]
        return "%d %d" % (pair[0], pair[1])
    step = (m - len(early) - 1) % len(rest)
    return "%d %d" % (biggest, rest[step])


# --- clause: main :: () -> None ---
def main():
    n, q, values, asks = read_input()
    state = warm_up(n, values)
    early, rest, biggest = state
    out = []
    for m in asks:
        out.append(answer_query(m, early, rest, biggest))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
