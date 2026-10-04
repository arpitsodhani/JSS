import sys

MOD = 998244353


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases


# --- clause: count_beautiful :: (values: list[int]) -> int ---
def count_beautiful(values):
    half = (MOD + 1) // 2
    power = 1
    inverse = 1
    ones = 0
    acc = 0
    total = 0
    for value in values:
        if value == 1:
            ones += 1
            acc = (acc + inverse) % MOD
        elif value == 2:
            power = power * 2 % MOD
            inverse = inverse * half % MOD
        else:
            total = (total + power * acc - ones) % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(count_beautiful(values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
