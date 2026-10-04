import sys

MOD = 1000000007


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        bits = data[pos + 1]
        pos += 2
        cases.append((n, bits))
    return cases


# --- clause: expected_ops :: (n: int, bits: bytes) -> int ---
def expected_ops(n, bits):
    half = (MOD + 1) // 2
    carry = 0
    for k in range(n - 1):
        if bits[n - 1 - k] == 49:
            carry = (1 + carry) * half % MOD
        else:
            carry = carry * half % MOD
    return (n - 1 + carry) % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, bits in read_input():
        out.append(str(expected_ops(n, bits)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
