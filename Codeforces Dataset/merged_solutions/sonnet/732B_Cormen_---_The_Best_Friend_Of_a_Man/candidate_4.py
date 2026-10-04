import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    days = [int(data[i + 2]) for i in range(n)]
    return n, k, days


# --- clause: plan_walks :: (n: int, k: int, days: list[int]) -> tuple[int, list[int]] ---
def plan_walks(n, k, days):
    plan = list(days)
    extra = 0
    for i in range(1, n):
        need = k - plan[i - 1]
        if plan[i] < need:
            extra += need - plan[i]
            plan[i] = need
    return extra, plan


# --- clause: main :: () -> None ---
def main():
    n, k, days = read_input()
    extra, plan = plan_walks(n, k, days)
    out = [str(extra), " ".join([str(value) for value in plan])]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
