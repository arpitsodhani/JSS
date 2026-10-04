import sys

# CLAUSE: setup_environment
MOD = 1000000007
INV2 = 500000004

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    k, n, m = data[0], data[1], data[2]
    at_zero = {}
    at_one = {}
    points = {k}
    if k > 1:
        points.add(k - 1)

    ptr = 3
    for _ in range(n):
        l = data[ptr]
        r = data[ptr + 1]
        ptr += 2
        at_zero[r] = max(at_zero.get(r, 0), l)
        points.add(r)
        if l > 1:
            points.add(l - 1)

    for _ in range(m):
        l = data[ptr]
        r = data[ptr + 1]
        ptr += 2
        at_one[r] = max(at_one.get(r, 0), l)
        points.add(r)
        if l > 1:
            points.add(l - 1)

    pref_zero = {0: 1}
    pref_one = {0: 1}
    ways_zero = 1
    ways_one = 1
    zero_limit = 0
    one_limit = 0
    pos = 0

    def move(length):
        nonlocal ways_zero, ways_one
        if length <= 0:
            return
        blocked_zero = 0 if zero_limit == 0 else pref_one[zero_limit - 1]
        blocked_one = 0 if one_limit == 0 else pref_zero[one_limit - 1]
        power = pow(2, length, MOD)
        total = (power * (ways_zero + ways_one) - (power - 1) * (blocked_zero + blocked_one)) % MOD
        ways_zero = (total + blocked_one - blocked_zero) * INV2 % MOD
        ways_one = (total - blocked_one + blocked_zero) * INV2 % MOD

    for x in sorted(points):
        if x <= 0 or x > k:
            continue
        if x in at_zero or x in at_one:
            move(x - 1 - pos)
            pos = x - 1
            if x in at_zero:
                zero_limit = max(zero_limit, at_zero[x])
            if x in at_one:
                one_limit = max(one_limit, at_one[x])
            move(1)
            pos = x
        else:
            move(x - pos)
            pos = x
        pref_zero[x] = ways_zero
        pref_one[x] = ways_one

    print((ways_zero + ways_one - pref_zero.get(k - 1, 1) - pref_one.get(k - 1, 1)) % MOD)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
