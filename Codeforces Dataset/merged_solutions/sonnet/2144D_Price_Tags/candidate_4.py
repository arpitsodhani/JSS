# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_one(n, y, prices):
    top = max(prices)
    if top == 1:
        return n

    frequency = [0] * (top + 2)
    for price in prices:
        frequency[price] += 1

    prefix = frequency[:]
    for i in range(1, top + 2):
        prefix[i] += prefix[i - 1]

    best = -10**30
    for x in range(2, top + 1):
        total_income = 0
        reusable_tags = 0
        left = 1
        reduced = 1
        for right in range(x, top + x, x):
            if left > top:
                break
            end = right if right <= top else top
            quantity = prefix[end] - prefix[left - 1]
            total_income += quantity * reduced
            if reduced <= top:
                own = frequency[reduced]
                reusable_tags += quantity if quantity < own else own
            left = end + 1
            reduced += 1
        candidate = total_income - (n - reusable_tags) * y
        if candidate > best:
            best = candidate
    return best

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    index = 1
    result = []
    for _ in range(t):
        n = int(raw[index])
        y = int(raw[index + 1])
        index += 2
        prices = [int(v) for v in raw[index:index + n]]
        index += n
        result.append(str(solve_one(n, y, prices)))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
