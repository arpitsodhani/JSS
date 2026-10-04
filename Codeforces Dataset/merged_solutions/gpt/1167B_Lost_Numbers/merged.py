# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
nums = [4, 8, 15, 16, 23, 42]
data = list(map(int, sys.stdin.read().split()))

if data:
    p = data[:4]
    ans = [0] * 6

    roots = {x * x: x for x in nums}
    if len(p) >= 4 and p[0] in roots and p[1] in roots:
        ans[0] = roots[p[0]]
        ans[1] = roots[p[1]]
        used = {ans[0], ans[1]}
        rem = [x for x in nums if x not in used]

        for x in rem:
            for y in rem:
                if x != y and x * y == p[2]:
                    ans[2], ans[4] = x, y
        used.update([ans[2], ans[4]])
        rem = [x for x in nums if x not in used]

        for x in rem:
            for y in rem:
                if x != y and x * y == p[3]:
                    ans[3], ans[5] = x, y

        print(*ans)
    else:
        prod12, prod23, prod45, prod56 = p
        for a in nums:
            if prod12 % a:
                continue
            b = prod12 // a
            if b not in nums or b == a:
                continue
            if prod23 % b:
                continue
            c = prod23 // b
            if c not in nums or c in (a, b):
                continue
            left = [x for x in nums if x not in (a, b, c)]
            for d in left:
                if prod45 % d:
                    continue
                e = prod45 // d
                if e not in left or e == d:
                    continue
                if prod56 % e:
                    continue
                f = prod56 // e
                if f in left and f not in (d, e):
                    print(a, b, c, d, e, f)
                    sys.exit()
else:
    queries = [(1, 2), (2, 3), (4, 5), (5, 6)]
    res = []
    for i, j in queries:
        print("?", i, j, flush=True)
        res.append(int(input()))

    prod12, prod23, prod45, prod56 = res

    for a in nums:
        if prod12 % a:
            continue
        b = prod12 // a
        if b not in nums or b == a:
            continue
        if prod23 % b:
            continue
        c = prod23 // b
        if c not in nums or c in (a, b):
            continue
        left = [x for x in nums if x not in (a, b, c)]
        for d in left:
            if prod45 % d:
                continue
            e = prod45 // d
            if e not in left or e == d:
                continue
            if prod56 % e:
                continue
            f = prod56 // e
            if f in left and f not in (d, e):
                print("!", a, b, c, d, e, f, flush=True)
                sys.exit()

# CLAUSE: finish_program
RESULT_SENTINEL = None
