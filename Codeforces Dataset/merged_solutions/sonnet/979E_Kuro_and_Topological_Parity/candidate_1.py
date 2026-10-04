import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    p = int(data[1])
    colours = [int(token) for token in data[2:n + 2]]
    return n, p, colours


# --- clause: count_ways :: (n: int, p: int, colours: list[int]) -> int ---
def count_ways(n, p, colours):
    states = {(0, 0, 0): 1}
    for i in range(1, n + 1):
        every = pow(2, i - 1, MOD)
        half = pow(2, i - 2, MOD) if i >= 2 else 0
        nxt = {}
        for key, ways in states.items():
            black_odd, white_odd, parity = key
            for colour in (0, 1):
                if colours[i - 1] != -1 and colours[i - 1] != colour:
                    continue
                opposite = black_odd if colour == 1 else white_odd
                grown_black = 1 if (colour == 0 or black_odd) else 0
                grown_white = 1 if (colour == 1 or white_odd) else 0
                if not opposite:
                    hit = (grown_black, grown_white, parity ^ 1)
                    nxt[hit] = (nxt.get(hit, 0) + ways * every) % MOD
                else:
                    hit = (grown_black, grown_white, parity ^ 1)
                    nxt[hit] = (nxt.get(hit, 0) + ways * half) % MOD
                    miss = (black_odd, white_odd, parity)
                    nxt[miss] = (nxt.get(miss, 0) + ways * half) % MOD
        states = nxt
    total = 0
    for key, ways in states.items():
        if key[2] == p:
            total += ways
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, p, colours = read_input()
    sys.stdout.write(str(count_ways(n, p, colours)) + "\n")


if __name__ == "__main__":
    main()
