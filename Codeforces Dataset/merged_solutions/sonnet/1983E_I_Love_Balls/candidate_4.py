import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        k = numbers[reader + 1]
        reader += 2
        cases.append((k, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: split_scores :: (k: int, values: list[int]) -> tuple[int, int] ---
def split_scores(k, values):
    mod = 10 ** 9 + 7
    special = 0
    plain = 0
    for i in range(len(values)):
        if i < k:
            special += values[i]
        else:
            plain += values[i]
    plenty = len(values) - k
    alice = special % mod * ((plenty + 2) // 2) % mod * pow(plenty + 1, mod - 2, mod) % mod
    bob = (special - alice) % mod
    if plenty:
        mine = plain % mod * ((plenty + 1) // 2) % mod * pow(plenty, mod - 2, mod) % mod
        alice = (alice + mine) % mod
        bob = (bob + plain - mine) % mod
    return alice % mod, bob % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, values in read_input():
        alice, bob = split_scores(k, values)
        out.append("%d %d" % (alice, bob))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
