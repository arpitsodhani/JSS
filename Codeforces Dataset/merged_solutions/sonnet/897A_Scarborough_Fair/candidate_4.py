import sys


# --- clause: read_input :: () -> tuple[int, int, bytearray, list] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    text = bytearray(data[2])
    steps = [(int(data[3 + 4 * i]), int(data[4 + 4 * i]),
              data[5 + 4 * i][0], data[6 + 4 * i][0]) for i in range(m)]
    return n, m, text, steps


# --- clause: apply_steps :: (n: int, text: bytearray, steps: list) -> bytearray ---
def apply_steps(n, text, steps):
    for l, r, old, new in steps:
        table = bytearray(range(256))
        table[old] = new
        text[l - 1:r] = text[l - 1:r].translate(bytes(table))
    return text


# --- clause: main :: () -> None ---
def main():
    n, m, text, steps = read_input()
    result = apply_steps(n, text, steps)
    sys.stdout.write(result.decode() + "\n")


if __name__ == "__main__":
    main()
