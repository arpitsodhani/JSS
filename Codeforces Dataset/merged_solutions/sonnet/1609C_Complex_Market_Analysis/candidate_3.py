# CLAUSE: setup_environment
import sys
from math import isqrt

def make_sieve(top):
    flags = bytearray(b"\x01") * (top + 1)
    if top >= 0:
        flags[0] = 0
    if top >= 1:
        flags[1] = 0
    for x in range(2, isqrt(top) + 1):
        if flags[x]:
            start = x * x
            flags[start:top + 1:x] = b"\x00" * (((top - start) // x) + 1)
    return flags

# CLAUSE: solve_logic
def count_for_array(n, e, arr, prime):
    answer = 0
    for offset in range(e):
        chain = arr[offset:n:e]
        stops = [-1]
        for i, value in enumerate(chain):
            if value != 1:
                stops.append(i)
        stops.append(len(chain))

        for j in range(1, len(stops) - 1):
            middle = stops[j]
            if prime[chain[middle]]:
                answer += (middle - stops[j - 1]) * (stops[j + 1] - middle) - 1
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    tests = []
    maximum = 0
    for _ in range(data[0]):
        n, e = data[at], data[at + 1]
        at += 2
        arr = data[at:at + n]
        at += n
        tests.append((n, e, arr))
        maximum = max(maximum, max(arr))

    prime = make_sieve(maximum)
    answers = [str(count_for_array(n, e, arr, prime)) for n, e, arr in tests]
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
