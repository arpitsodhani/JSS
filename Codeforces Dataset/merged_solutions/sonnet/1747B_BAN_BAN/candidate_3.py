import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = []
    for i in range(t):
        sizes.append(int(data[1 + i]))
    return sizes


# --- clause: plan_swaps :: (n: int) -> list[str] ---
def plan_swaps(n):
    moves = (n + 1) // 2
    out = [str(moves)]
    for i in range(moves):
        left = 3 * i + 2
        right = 3 * n - 3 * i
        out.append("%d %d" % (left, right))
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.extend(plan_swaps(n))
    print("\n".join(out))


if __name__ == "__main__":
    main()
