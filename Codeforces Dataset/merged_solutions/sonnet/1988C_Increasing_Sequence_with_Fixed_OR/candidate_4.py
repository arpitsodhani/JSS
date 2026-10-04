import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_sequence :: (n: int) -> list[int] ---
def build_sequence(n):
    bits = []
    entry = n
    while entry:
        low = entry & (-entry)
        bits.append(low)
        entry -= low
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
