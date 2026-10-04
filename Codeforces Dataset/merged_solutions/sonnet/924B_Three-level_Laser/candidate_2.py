import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    u = data[1]
    return n, u, data[2:2 + n]


# --- clause: best_efficiency :: (n: int, u: int, energy: list[int]) -> float ---
def best_efficiency(n, u, energy):
    best = -1.0
    for i in range(n - 2):
        lo = i + 2
        hi = n - 1
        found = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if energy[mid] - energy[i] <= u:
                found = mid
                lo = mid + 1
            else:
                hi = mid - 1
        if found < 0:
            continue
        here = (energy[found] - energy[i + 1]) / (energy[found] - energy[i])
        if here > best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    n, u, energy = read_input()
    best = best_efficiency(n, u, energy)
    if best < 0:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%.12f\n" % best)


if __name__ == "__main__":
    main()
