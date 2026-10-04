# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def legal_complete(a):
    n = len(a)
    for mid, val in enumerate(a):
        span = 1
        stop = min(mid + 1, n - mid)
        while span < stop:
            block = a[mid - span:mid + span + 1]
            if sorted(block)[span] == val:
                return False
            span += 1
    return True

def legal_partial(a):
    n = len(a)
    for mid in range(n):
        if a[mid] < 0:
            continue
        reach = min(mid + 1, n - mid)
        for d in range(1, reach):
            lo = mid - d
            hi = mid + d + 1
            bad = False
            for x in a[lo:hi]:
                if x < 0:
                    bad = True
                    break
            if bad:
                continue
            b = sorted(a[lo:hi])
            if b[d] == a[mid]:
                return False
    return True

def solve_case(n, a):
    taken = [False] * (n + 1)
    empty = []
    for i, x in enumerate(a):
        if x == -1:
            empty.append(i)
        else:
            taken[x] = True
    pool = []
    for x in range(1, n + 1):
        if not taken[x]:
            pool.append(x)
    if len(pool) != len(empty):
        return 0
    total = 0

    def put(i, remaining):
        nonlocal total
        if i == len(empty):
            if legal_complete(a):
                total += 1
                if total >= MOD:
                    total -= MOD
            return
        pos = empty[i]
        m = len(remaining)
        for j in range(m):
            val = remaining[j]
            a[pos] = val
            if legal_partial(a):
                put(i + 1, remaining[:j] + remaining[j + 1:])
            a[pos] = -1

    if legal_partial(a):
        put(0, pool)
    return total % MOD

# CLAUSE: finish_program
def main():
    nums = sys.stdin.buffer.read().split()
    if not nums:
        return
    q = int(nums[0])
    k = 1
    answers = []
    for _ in range(q):
        n = int(nums[k])
        k += 1
        arr = [int(x) for x in nums[k:k + n]]
        k += n
        answers.append(str(solve_case(n, arr)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
