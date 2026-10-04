# CLAUSE: setup_environment
import sys

def interval_near(value, low, high):
    return low - 1 <= value <= high + 1

# CLAUSE: solve_logic
def solve_one(a):
    n = len(a)
    previous = a[0]
    for current in a[1:]:
        if previous - 1 <= current <= previous + 1:
            return 0
        previous = current
    if n == 2:
        return -1
    best = n
    for left in range(n):
        low = high = a[left]
        right = left
        while right < n:
            val = a[right]
            if val < low:
                low = val
            elif val > high:
                high = val
            if left > 0 and interval_near(a[left - 1], low, high):
                ops = right - left
                if ops < best:
                    best = ops
            if right + 1 < n and interval_near(a[right + 1], low, high):
                ops = right - left
                if ops < best:
                    best = ops
            right += 1
    return -1 if best == n else best

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    answers = []
    for _ in range(t):
        n = int(data[p])
        p += 1
        a = [int(x) for x in data[p:p + n]]
        p += n
        answers.append(str(solve_one(a)))
    print("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
