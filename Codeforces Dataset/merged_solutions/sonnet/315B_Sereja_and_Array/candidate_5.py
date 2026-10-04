import sys


# --- clause: read_input :: () -> tuple[list[int], list[list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    a = raw[2:2 + n]
    offset = 2 + n
    steps = []
    for _ in range(m):
        kind = raw[offset]
        if kind == 1:
            steps.append([1, raw[offset + 1], raw[offset + 2]])
            offset += 3
        else:
            steps.append([kind, raw[offset + 1]])
            offset += 2
    return a, steps


# --- clause: run_steps :: (a: list[int], steps: list[list[int]]) -> list[int] ---
def run_steps(a, steps):
    shift = 0
    written = []
    for step in steps:
        if step[0] == 1:
            a[step[1] - 1] = step[2] - shift
        elif step[0] == 2:
            shift += step[1]
        else:
            written.append(a[step[1] - 1] + shift)
    return written


# --- clause: main :: () -> None ---
def main():
    a, steps = read_input()
    sys.stdout.write("\n".join(map(str, run_steps(a, steps))) + "\n")


if __name__ == "__main__":
    main()
