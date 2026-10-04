import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: build_sequence :: (n: int) -> list[int] ---
def build_sequence(n):
    bits = []
    number = n
    while number:
        bottom = number & (-number)
        bits.append(bottom)
        number -= bottom
    if len(bits) == 1:
        return [n]
    steps = sorted(n - bit for bit in bits)
    steps.append(n)
    return steps


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        steps = build_sequence(n)
        out.append(str(len(steps)))
        out.append(" ".join(map(str, steps)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
