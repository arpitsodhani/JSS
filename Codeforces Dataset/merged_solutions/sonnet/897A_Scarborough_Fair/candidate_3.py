import sys


# --- clause: read_input :: () -> tuple[int, int, bytearray, list] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    text = bytearray(data[2])
    steps = []
    pos = 3
    while len(steps) < m:
        steps.append((int(data[pos]), int(data[pos + 1]), data[pos + 2][0], data[pos + 3][0]))
        pos += 4
    return n, m, text, steps


# --- clause: apply_steps :: (n: int, text: bytearray, steps: list) -> bytearray ---
def apply_steps(n, text, steps):
    for step in steps:
        l, r, old, new = step
        i = l - 1
        while i < r:
            if text[i] == old:
                text[i] = new
            i += 1
    return text


# --- clause: main :: () -> None ---
def main():
    n, m, text, steps = read_input()
    print(apply_steps(n, text, steps).decode())


if __name__ == "__main__":
    main()
