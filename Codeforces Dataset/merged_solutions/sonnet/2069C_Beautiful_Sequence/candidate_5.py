import sys

MOD = 998244353


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases


# --- clause: count_beautiful :: (values: list[int]) -> int ---
def count_beautiful(values):
    n = len(values)
    twos = [0] * (n + 1)
    for i in range(n):
        twos[i + 1] = twos[i]
        if values[i] == 2:
            twos[i + 1] += 1
    top = twos[n]
    power = [1] * (top + 1)
    for i in range(1, top + 1):
        power[i] = power[i - 1] * 2 % MOD
    half = (MOD + 1) // 2
    inverse = [1] * (top + 1)
    for i in range(1, top + 1):
        inverse[i] = inverse[i - 1] * half % MOD
    acc = 0
    ones = 0
    total = 0
    for i in range(n):
        if values[i] == 1:
            ones += 1
            acc = (acc + inverse[twos[i]]) % MOD
        elif values[i] == 3:
            total = (total + power[twos[i]] * acc - ones) % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(count_beautiful(values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
