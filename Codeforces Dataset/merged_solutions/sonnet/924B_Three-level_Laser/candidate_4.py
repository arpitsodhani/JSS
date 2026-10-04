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
    pick = 1
    for i in range(n - 2):
        if pick < i + 2:
            pick = i + 2
        while pick + 1 < n and energy[pick + 1] - energy[i] <= u:
            pick += 1
        if energy[pick] - energy[i] > u:
            continue
        span = energy[pick] - energy[i]
        useful = energy[pick] - energy[i + 1]
        value = useful / span
        if value > best:
            best = value
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
