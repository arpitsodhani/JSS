import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: split_sets :: (n: int, values: list[int]) -> tuple[list[int], list[int], list[int]] ---
def split_sets(n, values):
    negatives = []
    positives = []
    zeros = []
    for value in values:
        if value < 0:
            negatives.append(value)
        elif value > 0:
            positives.append(value)
        else:
            zeros.append(value)
    first = [negatives[0]]
    rest = negatives[1:]
    if len(rest) % 2 == 1:
        zeros.append(rest[-1])
        rest = rest[:-1]
    second = positives + rest
    return first, second, zeros


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    groups = split_sets(n, values)
    first, second, zeros = groups
    out = []
    for group in [first, second, zeros]:
        parts = [str(len(group))]
        parts.extend(str(v) for v in group)
        out.append(" ".join(parts))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
