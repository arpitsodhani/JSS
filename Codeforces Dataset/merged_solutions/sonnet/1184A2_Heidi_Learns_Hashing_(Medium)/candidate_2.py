import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, bits = int(data[0]), data[1]
    return n, bits


# --- clause: totient :: (value: int) -> int ---
def totient(value):
    result = value
    rest = value
    factor = 2
    while factor * factor <= rest:
        if rest % factor == 0:
            result = result // factor * (factor - 1)
            while rest % factor == 0:
                rest //= factor
        factor += 1
    if rest > 1:
        result = result // rest * (rest - 1)
    return result


# --- clause: count_shifts :: (n: int, bits: bytes) -> int ---
def count_shifts(n, bits):
    total = 0
    for step in range(1, n + 1):
        if n % step:
            continue
        parity = [0] * step
        for i in range(n):
            parity[i % step] ^= bits[i] - 48
        good = True
        for value in parity:
            if value:
                good = False
                break
        if good:
            total += totient(n // step)
    return total


# --- clause: main :: () -> None ---
def main():
    n, bits = read_input()
    sys.stdout.write("%d\n" % count_shifts(n, bits))


if __name__ == "__main__":
    main()
