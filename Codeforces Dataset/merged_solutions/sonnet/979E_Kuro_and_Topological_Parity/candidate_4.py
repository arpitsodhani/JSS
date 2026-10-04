import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    p = int(data[1])
    colours = [int(data[i + 2]) for i in range(n)]
    return n, p, colours


# --- clause: count_ways :: (n: int, p: int, colours: list[int]) -> int ---
def count_ways(n, p, colours):
    states = {(0, 0, 0): 1}
    power = 1
    for i in range(1, n + 1):
        half = pow(2, i - 2, MOD) if i >= 2 else 0
        every = power
        power = power * 2 % MOD
        fresh = {}
        allowed = (0, 1) if colours[i - 1] == -1 else (colours[i - 1],)
        for state in states:
            ways = states[state]
            black_odd, white_odd, parity = state
            for colour in allowed:
                if colour == 0:
                    opposite = white_odd
                    nb, nw = 1, white_odd
                else:
                    opposite = black_odd
                    nb, nw = black_odd, 1
                if opposite:
                    key = (nb, nw, parity ^ 1)
                    fresh[key] = (fresh.get(key, 0) + ways * half) % MOD
                    fresh[state] = (fresh.get(state, 0) + ways * half) % MOD
                else:
                    key = (nb, nw, parity ^ 1)
                    fresh[key] = (fresh.get(key, 0) + ways * every) % MOD
        states = fresh
    answer = 0
    for state in states:
        if state[2] == p:
            answer = (answer + states[state]) % MOD
    return answer


# --- clause: main :: () -> None ---
def main():
    n, p, colours = read_input()
    answer = count_ways(n, p, colours)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
