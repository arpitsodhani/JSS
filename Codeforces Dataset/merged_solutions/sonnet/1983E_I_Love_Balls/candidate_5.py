import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        k = raw[offset + 1]
        offset += 2
        cases.append((k, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: split_scores :: (k: int, values: list[int]) -> tuple[int, int] ---
def split_scores(k, values):
    mod = 10 ** 9 + 7
    special = sum(values[:k]) % mod
    plain = sum(values[k:]) % mod
    gaps = len(values) - k + 1
    alice = special * ((gaps + 1) // 2) % mod * pow(gaps, mod - 2, mod) % mod
    if gaps > 1:
        share = gaps - 1
        alice = (alice + plain * ((share + 1) // 2) % mod * pow(share, mod - 2, mod)) % mod
    running = (special + plain) % mod
    return alice, (running - alice) % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, values in read_input():
        alice, bob = split_scores(k, values)
        out.append("%d %d" % (alice, bob))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
