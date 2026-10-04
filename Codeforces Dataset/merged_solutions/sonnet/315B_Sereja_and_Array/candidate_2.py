import sys


# --- clause: read_input :: () -> tuple[list[int], list[list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    a = tokens[2:2 + n]
    pos = 2 + n
    steps = []
    for _ in range(m):
        kind = tokens[pos]
        if kind == 1:
            steps.append([1, tokens[pos + 1], tokens[pos + 2]])
            pos += 3
        else:
            steps.append([kind, tokens[pos + 1]])
            pos += 2
    return a, steps


# --- clause: run_steps :: (a: list[int], steps: list[list[int]]) -> list[int] ---
def run_steps(a, steps):
    shift = 0
    lines = []
    for step in steps:
        if step[0] == 1:
            a[step[1] - 1] = step[2] - shift
        elif step[0] == 2:
            shift += step[1]
        else:
            lines.append(a[step[1] - 1] + shift)
    return lines


# --- clause: main :: () -> None ---
def main():
    a, steps = read_input()
    sys.stdout.write("\n".join(map(str, run_steps(a, steps))) + "\n")


if __name__ == "__main__":
    main()
