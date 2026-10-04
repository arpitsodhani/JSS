import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2]


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
    amount = 0
    for d in range(top + 1):
        opened = 1 if (started or d > 0) else 0
        marks = (mask | (1 << d)) if opened else 0
        c, s = walk_digits(digits, k, memo, pos + 1, marks, opened, 1 if (tight and d == top) else 0)
        count = (count + c) % mod
        amount = (amount + s + d * power % mod * c) % mod
    if not tight:
        memo[key] = (count, amount)
    return count, amount


# --- clause: sum_upto :: (limit: int, k: int) -> int ---
def sum_upto(limit, k):
    if limit <= 0:
        return 0
    digits = [int(ch) for ch in str(limit)]
    return walk_digits(digits, k, {}, 0, 0, 0, 1)[1]


# --- clause: main :: () -> None ---
def main():
    l, r, k = read_input()
    mod = 998244353
    sys.stdout.write("%d\n" % ((sum_upto(r, k) - sum_upto(l - 1, k)) % mod))


if __name__ == "__main__":
    main()
