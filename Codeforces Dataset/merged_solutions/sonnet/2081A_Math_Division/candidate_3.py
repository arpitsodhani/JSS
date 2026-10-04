import sys

MOD = 1000000007


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    while len(cases) < t:
        cases.append((int(data[pos]), data[pos + 1]))
        pos += 2
    return cases


# --- clause: expected_ops :: (n: int, bits: bytes) -> int ---
def expected_ops(n, bits):
    half = (MOD + 1) // 2
    total = 0
    for k in range(n - 1, 0, -1):
        if bits[k] == 49:
            total = (total + 1) * half % MOD
        else:
            total = total * half % MOD
    return (n - 1 + total) % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, bits in read_input():
        out.append(str(expected_ops(n, bits)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
