import sys
from array import array

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    return data[2:2 + n], data[2 + n:2 + n + m]

# Clause smallest_factors [Confidence: 1.00]
def smallest_factors(limit):
    least = array('i', [0]) * (limit + 1)
    element = 2
    while element * element <= limit:
        if least[element] == 0:
            jump = element * element
            while jump <= limit:
                if least[jump] == 0:
                    least[jump] = element
                jump += element
        element += 1
    return least

# Clause shared_powers [Confidence: 1.00]
def shared_powers(top, bottom, least):
    counts = [{}, {}]
    for side in (0, 1):
        for element in (top, bottom)[side]:
            while element > 1:
                prime = least[element] if least[element] else element
                counts[side][prime] = counts[side].get(prime, 0) + 1
                element //= prime
    shared = {}
    for prime in counts[0]:
        if prime in counts[1]:
            here = counts[0][prime]
            there = counts[1][prime]
            shared[prime] = here if here < there else there
    return shared

# Clause strip_shared [Confidence: 1.00]
def strip_shared(values, shared, least):
    out = []
    for element in values:
        kept = 1
        while element > 1:
            prime = least[element] if least[element] else element
            element //= prime
            if shared.get(prime, 0) > 0:
                shared[prime] -= 1
            else:
                kept *= prime
        out.append(kept)
    return out

# Clause main [Confidence: 1.00]
def main():
    top, bottom = read_input()
    limit = max(max(top), max(bottom))
    least = smallest_factors(limit)
    shared = shared_powers(top, bottom, least)
    left = strip_shared(top, dict(shared), least)
    right = strip_shared(bottom, dict(shared), least)
    sys.stdout.write("%d %d\n%s\n%s\n" % (len(left), len(right),
                                          " ".join(map(str, left)),
                                          " ".join(map(str, right))))


if __name__ == "__main__":
    main()

