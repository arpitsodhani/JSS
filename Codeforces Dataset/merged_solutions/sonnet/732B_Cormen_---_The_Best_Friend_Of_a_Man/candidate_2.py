import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    days = list(map(int, data[2:n + 2]))
    return n, k, days


# --- clause: plan_walks :: (n: int, k: int, days: list[int]) -> tuple[int, list[int]] ---
def plan_walks(n, k, days):
    plan = days[:]
    extra = 0
    for i in range(1, n):
        pair = plan[i - 1] + plan[i]
        if pair < k:
            plan[i] += k - pair
            extra += k - pair
    return extra, plan


# --- clause: main :: () -> None ---
def main():
    n, k, days = read_input()
    extra, plan = plan_walks(n, k, days)
    sys.stdout.write("%d\n%s\n" % (extra, " ".join(map(str, plan))))


if __name__ == "__main__":
    main()
