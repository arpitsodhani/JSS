import sys
from array import array


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    return tokens[2:2 + n], tokens[2 + n:2 + n + m]


# --- clause: smallest_factors :: (limit: int) -> array ---
def smallest_factors(limit):
    least = array('i', [0]) * (limit + 1)
    item = 2
    while item * item <= limit:
        if least[item] == 0:
            step = item * item
            while step <= limit:
                if least[step] == 0:
                    least[step] = item
                step += item
        item += 1
    return least


# --- clause: shared_powers :: (top: list[int], bottom: list[int], least: array) -> dict[int, int] ---
def shared_powers(top, bottom, least):
    counts = [{}, {}]
    for side in (0, 1):
        for item in (top, bottom)[side]:
            while item > 1:
                prime = least[item] if least[item] else item
                counts[side][prime] = counts[side].get(prime, 0) + 1
                item //= prime
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
    for item in values:
        kept = 1
        while item > 1:
            prime = least[item] if least[item] else item
            item //= prime
            if shared.get(prime, 0) > 0:
                shared[prime] -= 1
            else:
                kept *= prime
        out.append(kept)
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
