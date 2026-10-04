import sys

MOD = 1000000007


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        bits = data[pos]
        pos += 1
        cases.append((n, bits))
    return cases


# --- clause: expected_ops :: (n: int, bits: bytes) -> int ---
def expected_ops(n, bits):
    half = (MOD + 1) // 2
    tail = bits[1:]
    carry = 0
    for byte in reversed(tail):
        step = 1 if byte == 49 else 0
        carry = (carry + step) * half % MOD
    return (n - 1 + carry) % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, bits in read_input():
        out.append(str(expected_ops(n, bits)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
