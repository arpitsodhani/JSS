import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])

# Clause prime_prefix [Confidence: 1.00]
def prime_prefix(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    step = 2
    while step * step <= limit:
        if sieve[step]:
            sieve[step * step::step] = bytearray(len(sieve[step * step::step]))
        step += 1
    prefix = [0] * (limit + 2)
    for value in range(1, limit + 1):
        prefix[value] = prefix[value - 1] + sieve[value]
    return prefix

# Clause shortest_window [Confidence: 1.00]
def shortest_window(a, b, k, prefix):
    lo = 1
    hi = b - a + 1
    answer = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        ok = True
        for x in range(a, b - mid + 2):
            if prefix[x + mid - 1] - prefix[x - 1] < k:
                ok = False
                break
        if ok:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer

# Clause main [Confidence: 1.00]
def main():
    a, b, k = read_input()
    prefix = prime_prefix(b)
    sys.stdout.write(str(shortest_window(a, b, k, prefix)) + "\n")


if __name__ == "__main__":
    main()

