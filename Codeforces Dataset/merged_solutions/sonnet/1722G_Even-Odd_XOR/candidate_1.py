import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


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
    high = 1 << 28
    taller = 1 << 29
    if (n - 3) % 2:
        values.append(high)
        values.append(taller)
        values.append(high ^ taller ^ even ^ odd)
    else:
        values.append(high)
        values.append(high ^ taller ^ even ^ odd)
        values.append(taller)
    return values


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
