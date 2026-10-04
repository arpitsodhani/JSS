import sys


# --- clause: read_input :: () -> tuple[int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), bytes(data[1])


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
    divisors = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            divisors.append(d)
            if d != n // d:
                divisors.append(n // d)
        d += 1
    for step in sorted(divisors):
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
    answer = count_shifts(n, bits)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
