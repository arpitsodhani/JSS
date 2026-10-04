import sys
from array import array


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    return numbers[2:2 + n], numbers[2 + n:2 + n + m]


# --- clause: smallest_factors :: (limit: int) -> array ---
def smallest_factors(limit):
    least = array('i', [0]) * (limit + 1)
    entry = 2
    while entry * entry <= limit:
        if least[entry] == 0:
            step = entry * entry
            while step <= limit:
                if least[step] == 0:
                    least[step] = entry
                step += entry
        entry += 1
    return least


# --- clause: shared_powers :: (top: list[int], bottom: list[int], least: array) -> dict[int, int] ---
def shared_powers(top, bottom, least):
    counts = [{}, {}]
    for side in (0, 1):
        for entry in (top, bottom)[side]:
            while entry > 1:
                prime = least[entry] if least[entry] else entry
                counts[side][prime] = counts[side].get(prime, 0) + 1
                entry //= prime
    shared = {}
    for prime in counts[0]:
        if prime in counts[1]:
            here = counts[0][prime]
            there = counts[1][prime]
            shared[prime] = here if here < there else there
    return shared


# --- clause: strip_shared :: (values: list[int], shared: dict[int, int], least: array) -> list[int] ---
def strip_shared(values, shared, least):
    out = []
    for value in values:
        for prime in shared:
            while shared[prime] > 0 and value % prime == 0:
                value //= prime
                shared[prime] -= 1
        out.append(value)
    return out


# --- clause: main :: () -> None ---
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
