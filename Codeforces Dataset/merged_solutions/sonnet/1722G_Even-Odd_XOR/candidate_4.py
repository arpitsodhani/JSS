import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    values = []
    for value in range(n - 3):
        values.append(value)
    mixed = 0
    for i in range(n - 3):
        mixed ^= values[i] if i % 2 == (n - 3) % 2 else 0
    even = 0
    odd = 0
    for i in range(len(values)):
        if i % 2:
            odd ^= values[i]
        else:
            even ^= values[i]
    first = 1 << 28
    second = 1 << 29
    third = first ^ second ^ even ^ odd
    if len(values) % 2:
        return values + [first, second, third]
    return values + [first, third, second]


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
