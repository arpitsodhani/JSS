import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    values = list(range(n - 3))
    even = 0
    odd = 0
    for i in range(n - 3):
        if i % 2:
            odd ^= values[i]
        else:
            even ^= values[i]
    top_value = 1 << 28
    taller = 1 << 29
    if (n - 3) % 2:
        values.append(top_value)
        values.append(taller)
        values.append(top_value ^ taller ^ even ^ odd)
    else:
        values.append(top_value)
        values.append(top_value ^ taller ^ even ^ odd)
        values.append(taller)
    return values


# --- clause: main :: () -> None ---
def main():
    written = []
    for n in read_input():
        written.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
