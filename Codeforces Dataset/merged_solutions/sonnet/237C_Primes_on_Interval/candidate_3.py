import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])


# --- clause: prime_prefix :: (limit: int) -> list[int] ---
def prime_prefix(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for step in range(2, int(limit ** 0.5) + 1):
        if sieve[step]:
            span = len(range(step * step, limit + 1, step))
            sieve[step * step::step] = bytearray(span)
    prefix = [0] * (limit + 2)
    for value in range(1, limit + 1):
        prefix[value] = prefix[value - 1] + sieve[value]
    return prefix


# --- clause: shortest_window :: (a: int, b: int, k: int, prefix: list[int]) -> int ---
def shortest_window(a, b, k, prefix):
    lo = 1
    hi = b - a + 1
    answer = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        ok = True
        x = a
        while x <= b - mid + 1:
            if prefix[x + mid - 1] - prefix[x - 1] < k:
                ok = False
                break
            x += 1
        if ok:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


# --- clause: main :: () -> None ---
def main():
    a, b, k = read_input()
    prefix = prime_prefix(b)
    print(shortest_window(a, b, k, prefix))


if __name__ == "__main__":
    main()
