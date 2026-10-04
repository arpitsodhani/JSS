import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    s = data[2]
    bugs = data[3:3 + m]
    skill = data[3 + m:3 + m + n]
    price = data[3 + m + n:3 + m + 2 * n]
    return s, bugs, skill, price

# Clause try_days [Confidence: 1.00]
def try_days(days, s, order, bugs, ranked, skill, price):
    m = len(bugs)
    n = len(skill)
    plan = [0] * m
    pool = []
    spent = 0
    ptr = 0
    at = 0
    while at < m:
        hardest = bugs[order[at]]
        while ptr < n and skill[ranked[ptr]] >= hardest:
            heapq.heappush(pool, (price[ranked[ptr]], ranked[ptr]))
            ptr += 1
        if not pool:
            return None
        cost, who = heapq.heappop(pool)
        spent += cost
        if spent > s:
            return None
        closing = at + days
        if closing > m:
            closing = m
        while at < closing:
            plan[order[at]] = who + 1
            at += 1
    return plan

# Clause fewest_days [Confidence: 1.00]
def fewest_days(s, bugs, skill, price):
    m = len(bugs)
    order = sorted(range(m), key=lambda i: -bugs[i])
    ranked = sorted(range(len(skill)), key=lambda i: -skill[i])
    best = None
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        plan = try_days(mid, s, order, bugs, ranked, skill, price)
        if plan is None:
            low = mid + 1
        else:
            best = plan
            high = mid - 1
    return best

# Clause main [Confidence: 1.00]
def main():
    s, bugs, skill, price = read_input()
    plan = fewest_days(s, bugs, skill, price)
    if plan is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n" + " ".join(map(str, plan)) + "\n")


if __name__ == "__main__":
    main()

