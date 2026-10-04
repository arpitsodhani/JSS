# Clause setup_environment [Confidence: 0.40]
import sys

MOD = 1000000007


# Clause solve_logic [Confidence: 0.60]
def valid_after_set(p, changed):
    n = len(p)
    left = changed
    right = changed
    for center in range(n):
        if p[center] == -1:
            continue
        limit = min(center, n - 1 - center)
        for radius in range(1, limit + 1):
            if not (center - radius <= changed <= center + radius):
                continue
            low = center - radius
            high = center + radius
            cnt = 0
            unknown = False
            for i in range(low, high + 1):
                if p[i] == -1:
                    unknown = True
                    break
                if p[i] < p[center]:
                    cnt += 1
            if not unknown and cnt == radius:
                return False
    return True

def initial_ok(p):
    n = len(p)
    for center in range(n):
        if p[center] == -1:
            continue
        for radius in range(1, min(center + 1, n - center)):
            segment = p[center - radius:center + radius + 1]
            if -1 in segment:
                continue
            smaller = sum(1 for x in segment if x < p[center])
            if smaller == radius:
                return False
    return True

def answer_one(n, p):
    seen = set()
    for x in p:
        if x != -1:
            seen.add(x)
    missing = set(range(1, n + 1)) - seen
    spots = [i for i, x in enumerate(p) if x == -1]
    if len(missing) != len(spots):
        return 0
    if not initial_ok(p):
        return 0
    result = 0

    def go(idx):
        nonlocal result
        if idx == len(spots):
            result = (result + 1) % MOD
            return
        pos = spots[idx]
        for val in tuple(missing):
            p[pos] = val
            missing.remove(val)
            if valid_after_set(p, pos):
                go(idx + 1)
            missing.add(val)
            p[pos] = -1

    go(0)
    return result


# Clause finish_program [Confidence: 0.80]
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


