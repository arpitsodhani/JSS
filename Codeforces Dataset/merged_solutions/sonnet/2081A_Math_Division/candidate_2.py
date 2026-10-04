import sys

MOD = 1000000007


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    cases = []
    for _ in range(t):
        n = int(data[idx])
        cases.append((n, data[idx + 1]))
        idx += 2
    return cases


# --- clause: expected_ops :: (n: int, bits: bytes) -> int ---
def expected_ops(n, bits):
    half = pow(2, MOD - 2, MOD)
    carry = 0
    for byte in bits[:0:-1]:
        if byte == 49:
            carry = (carry + 1) * half % MOD
        else:
            carry = carry * half % MOD
    return (carry + n - 1) % MOD


# --- clause: main :: () -> None ---
def main():
    answers = []
    for n, bits in read_input():
        answers.append(str(expected_ops(n, bits)))
    sys.stdout.write("%s\n" % "\n".join(answers))


if __name__ == "__main__":
    main()
