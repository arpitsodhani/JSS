import sys


# --- clause: read_input :: () -> tuple[int, int, bytearray, list] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    text = bytearray(data[2])
    steps = []
    idx = 3
    for _ in range(m):
        steps.append((int(data[idx]), int(data[idx + 1]), data[idx + 2][0], data[idx + 3][0]))
        idx += 4
    return n, m, text, steps


# --- clause: apply_steps :: (n: int, text: bytearray, steps: list) -> bytearray ---
def apply_steps(n, text, steps):
    for l, r, old, new in steps:
        chunk = text[l - 1:r]
        text[l - 1:r] = chunk.replace(bytes([old]), bytes([new]))
    return text


# --- clause: main :: () -> None ---
def main():
    n, m, text, steps = read_input()
    sys.stdout.write("%s\n" % apply_steps(n, text, steps).decode())


if __name__ == "__main__":
    main()
