import sys
from bisect import bisect_right


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    a = data[2:2 + n]
    shots = data[2 + n:2 + n + q]
    return n, q, a, shots

# --- clause: standing_counts :: (n: int, a: list[int], shots: list[int]) -> list[int] ---
def standing_counts(n, a, shots):
    prefix = [0] * (n + 1)
    for i, value in enumerate(a):
        prefix[i + 1] = prefix[i] + value
    total = prefix[n]
    out = []
    fired = 0
    for arrows in shots:
        fired += arrows
        if fired >= total:
            fired = 0
            out.append(n)
        else:
            out.append(n + 1 - bisect_right(prefix, fired))
    return out

# --- clause: main :: () -> None ---
def main():
    n, q, a, shots = read_input()
    sys.stdout.write("\n".join(map(str, standing_counts(n, a, shots))) + "\n")


if __name__ == "__main__":
    main()
