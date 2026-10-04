import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    p = int(data[1])
    colours = []
    for token in data[2:n + 2]:
        colours.append(int(token))
    return n, p, colours


# --- clause: count_ways :: (n: int, p: int, colours: list[int]) -> int ---
def count_ways(n, p, colours):
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = powers[i - 1] * 2 % MOD
    states = [0] * 8
    states[0] = 1
    for i in range(1, n + 1):
        every = powers[i - 1]
        half = powers[i - 2] if i >= 2 else 0
        fresh = [0] * 8
        want = colours[i - 1]
        for code in range(8):
            ways = states[code]
            if not ways:
                continue
            black_odd = code & 1
            white_odd = code >> 1 & 1
            parity = code >> 2 & 1
            for colour in (0, 1):
                if want >= 0 and want != colour:
                    continue
                opposite = black_odd if colour == 1 else white_odd
                nb = black_odd | (1 - colour)
                nw = white_odd | colour
                hit = nb | nw << 1 | (parity ^ 1) << 2
                if opposite:
                    fresh[hit] = (fresh[hit] + ways * half) % MOD
                    fresh[code] = (fresh[code] + ways * half) % MOD
                else:
                    fresh[hit] = (fresh[hit] + ways * every) % MOD
        states = fresh
    total = 0
    for code in range(8):
        if code >> 2 & 1 == p:
            total += states[code]
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, p, colours = read_input()
    print(count_ways(n, p, colours))


if __name__ == "__main__":
    main()
