import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    days = []
    for token in data[2:n + 2]:
        days.append(int(token))
    return n, k, days


# --- clause: plan_walks :: (n: int, k: int, days: list[int]) -> tuple[int, list[int]] ---
def plan_walks(n, k, days):
    plan = list(days)
    extra = 0
    i = 1
    while i < n:
        short = k - plan[i - 1] - plan[i]
        if short > 0:
            plan[i] = plan[i] + short
            extra = extra + short
        i += 1
    return extra, plan


# --- clause: main :: () -> None ---
def main():
    n, k, days = read_input()
    extra, plan = plan_walks(n, k, days)
    print(extra)
    print(" ".join(map(str, plan)))


if __name__ == "__main__":
    main()
