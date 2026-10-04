import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, p = int(data[0]), int(data[1])
    colours = list(map(int, data[2:n + 2]))
    return n, p, colours


# --- clause: count_ways :: (n: int, p: int, colours: list[int]) -> int ---
def count_ways(n, p, colours):
    states = [[[0] * 2 for _ in range(2)] for _ in range(2)]
    states[0][0][0] = 1
    for i in range(1, n + 1):
        every = pow(2, i - 1, MOD)
        half = pow(2, i - 2, MOD) if i >= 2 else 0
        fresh = [[[0] * 2 for _ in range(2)] for _ in range(2)]
        want = colours[i - 1]
        for black_odd in range(2):
            for white_odd in range(2):
                for parity in range(2):
                    ways = states[black_odd][white_odd][parity]
                    if not ways:
                        continue
                    for colour in range(2):
                        if want != -1 and want != colour:
                            continue
                        opposite = black_odd if colour else white_odd
                        nb = 1 if (colour == 0 or black_odd) else 0
                        nw = 1 if (colour == 1 or white_odd) else 0
                        if opposite:
                            fresh[nb][nw][parity ^ 1] += ways * half
                            fresh[black_odd][white_odd][parity] += ways * half
                        else:
                            fresh[nb][nw][parity ^ 1] += ways * every
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    fresh[a][b][c] %= MOD
        states = fresh
    total = 0
    for a in range(2):
        for b in range(2):
            total += states[a][b][p]
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, p, colours = read_input()
    sys.stdout.write("%d\n" % count_ways(n, p, colours))


if __name__ == "__main__":
    main()
