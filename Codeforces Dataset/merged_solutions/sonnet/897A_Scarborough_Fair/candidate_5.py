import sys


# --- clause: read_input :: () -> tuple[int, int, bytearray, list] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    text = bytearray(data[2])
    steps = []
    pos = 3
    for _ in range(m):
        l = int(data[pos])
        pos += 1
        r = int(data[pos])
        pos += 1
        old = data[pos][0]
        pos += 1
        new = data[pos][0]
        pos += 1
        steps.append((l, r, old, new))
    return n, m, text, steps


# --- clause: apply_steps :: (n: int, text: bytearray, steps: list) -> bytearray ---
def apply_steps(n, text, steps):
    for l, r, old, new in steps:
        for i, ch in enumerate(text[l - 1:r], start=l - 1):
            if ch == old:
                text[i] = new
    return text


# --- clause: main :: () -> None ---
def main():
    n, m, text, steps = read_input()
    sys.stdout.write(apply_steps(n, text, steps).decode() + "\n")


if __name__ == "__main__":
    main()
