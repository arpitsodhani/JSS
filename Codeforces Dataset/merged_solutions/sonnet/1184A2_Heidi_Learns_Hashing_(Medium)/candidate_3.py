import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0].decode()), data[1]


# --- clause: totient :: (value: int) -> int ---
def totient(value):
    result = value
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            while value % factor == 0:
                value //= factor
            result -= result // factor
        factor += 1
    if value > 1:
        result -= result // value
    return result


# --- clause: count_shifts :: (n: int, bits: bytes) -> int ---
def count_shifts(n, bits):
    total = 0
    for step in range(1, n + 1):
        if n % step:
            continue
        parity = [0] * step
        slot = 0
        for i in range(n):
            parity[slot] ^= bits[i] - 48
            slot += 1
            if slot == step:
                slot = 0
        if not any(parity):
            total += totient(n // step)
    return total


# --- clause: main :: () -> None ---
def main():
    n, bits = read_input()
    print(count_shifts(n, bits))


if __name__ == "__main__":
    main()
