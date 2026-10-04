import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    u = data[1]
    return n, u, data[2:2 + n]


# --- clause: best_efficiency :: (n: int, u: int, energy: list[int]) -> float ---
def best_efficiency(n, u, energy):
    answer = -1.0
    right = 2
    for i in range(n - 2):
        if right < i + 2:
            right = i + 2
        while right < n and energy[right] - energy[i] <= u:
            right += 1
        pick = right - 1
        if pick < i + 2:
            continue
        gain = (energy[pick] - energy[i + 1]) / (energy[pick] - energy[i])
        if gain > answer:
            answer = gain
    return answer


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
