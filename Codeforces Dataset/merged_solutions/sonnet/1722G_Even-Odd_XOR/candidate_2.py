import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    items = list(range(n - 3))
    even = 0
    odd = 0
    for i in range(n - 3):
        if i % 2:
            odd ^= items[i]
        else:
            even ^= items[i]
    high = 1 << 28
    taller = 1 << 29
    if (n - 3) % 2:
        items.append(high)
        items.append(taller)
        items.append(high ^ taller ^ even ^ odd)
    else:
        items.append(high)
        items.append(high ^ taller ^ even ^ odd)
        items.append(taller)
    return items


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
