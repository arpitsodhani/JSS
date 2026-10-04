import heapq
import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    s = numbers[2]
    bugs = numbers[3:3 + m]
    skill = numbers[3 + m:3 + m + n]
    price = numbers[3 + m + n:3 + m + 2 * n]
    return s, bugs, skill, price


# --- clause: try_days :: (days: int, s: int, order: list[int], bugs: list[int], ranked: list[int], skill: list[int], price: list[int]) -> list[int] | None ---
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
        end_here = at + days
        if end_here > m:
            end_here = m
        while at < end_here:
            plan[order[at]] = who + 1
            at += 1
    return plan


# --- clause: fewest_days :: (s: int, bugs: list[int], skill: list[int], price: list[int]) -> list[int] | None ---
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


# --- clause: main :: () -> None ---
def main():
    s, bugs, skill, price = read_input()
    plan = fewest_days(s, bugs, skill, price)
    if plan is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n" + " ".join(map(str, plan)) + "\n")


if __name__ == "__main__":
    main()
