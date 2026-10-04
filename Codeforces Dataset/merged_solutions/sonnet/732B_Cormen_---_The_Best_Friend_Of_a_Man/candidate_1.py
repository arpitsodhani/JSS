import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    days = [int(token) for token in data[2:n + 2]]
    return n, k, days


# --- clause: plan_walks :: (n: int, k: int, days: list[int]) -> tuple[int, list[int]] ---
def plan_walks(n, k, days):
    plan = list(days)
    extra = 0
    for i in range(1, n):
        short = k - plan[i - 1] - plan[i]
        if short > 0:
            plan[i] += short
            extra += short
    return extra, plan


# --- clause: main :: () -> None ---
def main():
    n, k, days = read_input()
    extra, plan = plan_walks(n, k, days)
    sys.stdout.write(str(extra) + "\n")
    sys.stdout.write(" ".join(map(str, plan)) + "\n")


if __name__ == "__main__":
    main()
