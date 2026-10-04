import sys
MOD = 1000000007

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    p = int(data[1])
    colours = list(map(int, data[2:2 + n]))
    return n, p, colours

# Clause count_ways [Confidence: 0.60]
def count_ways(n, p, colours):
    states = {(0, 0, 0): 1}
    for i in range(1, n + 1):
        every = pow(2, i - 1, MOD)
        half = every * pow(2, MOD - 2, MOD) % MOD if i >= 2 else 0
        fresh = {}
        for key in states:
            ways = states[key]
            black_odd, white_odd, parity = key
            for colour in (0, 1):
                if colours[i - 1] != -1 and colours[i - 1] != colour:
                    continue
                opposite = white_odd if colour == 0 else black_odd
                nb = 1 if colour == 0 else black_odd
                nw = 1 if colour == 1 else white_odd
                hit = (nb, nw, parity ^ 1)
                if opposite:
                    fresh[hit] = (fresh.get(hit, 0) + ways * half) % MOD
                    fresh[key] = (fresh.get(key, 0) + ways * half) % MOD
                else:
                    fresh[hit] = (fresh.get(hit, 0) + ways * every) % MOD
        states = fresh
    total = 0
    for key in states:
        if key[2] == p:
            total = (total + states[key]) % MOD
    return total % MOD

# Clause main [Confidence: 1.00]
def main():
    n, p, colours = read_input()
    sys.stdout.write(str(count_ways(n, p, colours)) + "\n")


if __name__ == "__main__":
    main()

