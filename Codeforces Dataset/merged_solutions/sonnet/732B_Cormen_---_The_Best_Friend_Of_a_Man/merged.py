import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    days = list(map(int, data[2:2 + n]))
    return n, k, days

# Clause plan_walks [Confidence: 0.80]
def plan_walks(n, k, days):
    plan = list(days)
    extra = 0
    for i in range(1, n):
        short = k - plan[i - 1] - plan[i]
        if short > 0:
            plan[i] += short
            extra += short
    return extra, plan

# Clause main [Confidence: 1.00]
def main():
    n, k, days = read_input()
    total, plan = plan_walks(n, k, days)
    sys.stdout.write(str(total) + "\n" + " ".join(map(str, plan)) + "\n")


if __name__ == "__main__":
    main()

