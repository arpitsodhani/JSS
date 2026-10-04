import sys


# --- clause: read_input :: () -> tuple[list[int], list[list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    a = fields[2:2 + n]
    cursor = 2 + n
    steps = []
    for _ in range(m):
        kind = fields[cursor]
        if kind == 1:
            steps.append([1, fields[cursor + 1], fields[cursor + 2]])
            cursor += 3
        else:
            steps.append([kind, fields[cursor + 1]])
            cursor += 2
    return a, steps


# --- clause: run_steps :: (a: list[int], steps: list[list[int]]) -> list[int] ---
def run_steps(a, steps):
    shift = 0
    collected = []
    for step in steps:
        if step[0] == 1:
            a[step[1] - 1] = step[2] - shift
        elif step[0] == 2:
            shift += step[1]
        else:
            collected.append(a[step[1] - 1] + shift)
    return collected


# --- clause: main :: () -> None ---
def main():
    a, steps = read_input()
    sys.stdout.write("\n".join(map(str, run_steps(a, steps))) + "\n")


if __name__ == "__main__":
    main()
