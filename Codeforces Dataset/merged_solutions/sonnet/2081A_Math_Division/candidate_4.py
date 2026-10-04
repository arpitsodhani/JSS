import sys

MOD = 1000000007


# --- clause: read_input :: () -> list[tuple[int, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[2 * i + 1]), data[2 * i + 2]) for i in range(t)]


# --- clause: expected_ops :: (n: int, bits: bytes) -> int ---
def expected_ops(n, bits):
    half = (MOD + 1) // 2
    carry = 0
    index = n - 1
    while index > 0:
        if bits[index] == 49:
            carry = (carry + 1) * half
        else:
            carry = carry * half
        carry %= MOD
        index -= 1
    return (n - 1 + carry) % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(expected_ops(case[0], case[1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
