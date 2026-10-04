import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
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
    rest = negatives[1:]
    first = [negatives[0]]
    if len(rest) % 2 == 1:
        zeros.append(rest[-1])
        rest = rest[:-1]
    second = list(positives)
    second.extend(rest)
    return first, second, zeros


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    first, second, zeros = split_sets(n, values)
    out = []
    for group in (first, second, zeros):
        out.append(str(len(group)) + " " + " ".join(map(str, group)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
