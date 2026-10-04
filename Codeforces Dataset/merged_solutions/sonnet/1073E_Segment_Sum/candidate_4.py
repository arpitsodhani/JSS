import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: walk_digits :: (digits: list[int], k: int, memo: dict, pos: int, mask: int, started: int, tight: int) -> tuple[int, int] ---
def walk_digits(digits, k, memo, pos, mask, started, tight):
    mod = 998244353
    if pos == len(digits):
        if started and bin(mask).count("1") <= k:
            return 1, 0
        return 0, 0
    key = (pos, mask, started)
    if not tight and key in memo:
        return memo[key]
    top = digits[pos] if tight else 9
    power = pow(10, len(digits) - pos - 1, mod)
    count = 0
    summed = 0
    for d in range(top + 1):
        opened = 1 if (started or d > 0) else 0
        marks = (mask | (1 << d)) if opened else 0
        c, s = walk_digits(digits, k, memo, pos + 1, marks, opened, 1 if (tight and d == top) else 0)
        count = (count + c) % mod
        summed = (summed + s + d * power % mod * c) % mod
    if not tight:
        memo[key] = (count, summed)
    return count, summed


# --- clause: sum_upto :: (limit: int, k: int) -> int ---
def sum_upto(limit, k):
    if limit <= 0:
        return 0
    mod = 998244353
    digits = [int(ch) for ch in str(limit)]
    n = len(digits)
    states = {}
    head = 0
    tight_mask = 0
    tight_started = 0
    for pos in range(n):
        fresh = {}
        for spot in states:
            mask, started = spot
            count, value = states[spot]
            for d in range(10):
                opened = 1 if (started or d > 0) else 0
                marks = (mask | (1 << d)) if opened else 0
                if bin(marks).count("1") > k:
                    continue
                key = (marks, opened)
                c, s = fresh.get(key, (0, 0))
                fresh[key] = ((c + count) % mod, (s + value * 10 + d * count) % mod)
        for d in range(digits[pos]):
            opened = 1 if (tight_started or d > 0) else 0
            marks = (tight_mask | (1 << d)) if opened else 0
            if bin(marks).count("1") > k:
                continue
            key = (marks, opened)
            c, s = fresh.get(key, (0, 0))
            fresh[key] = ((c + 1) % mod, (s + head * 10 + d) % mod)
        head = (head * 10 + digits[pos]) % mod
        tight_started = 1 if (tight_started or digits[pos] > 0) else 0
        tight_mask = (tight_mask | (1 << digits[pos])) if tight_started else 0
        states = fresh
    total = 0
    for spot in states:
        mask, started = spot
        if started and bin(mask).count("1") <= k:
            total = (total + states[spot][1]) % mod
    if tight_started and bin(tight_mask).count("1") <= k:
        total = (total + limit) % mod
    return total % mod


# --- clause: main :: () -> None ---
def main():
    l, r, k = read_input()
    mod = 998244353
    sys.stdout.write("%d\n" % ((sum_upto(r, k) - sum_upto(l - 1, k)) % mod))


if __name__ == "__main__":
    main()
