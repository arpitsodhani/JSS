# Clause setup_environment [Confidence: 0.75]
import sys

def tri(v):
    return v * (v + 1) // 2

def tail(days, length):
    if length <= 0:
        return 0
    return tri(days) - tri(days - length)


# Clause solve_logic [Confidence: 0.75]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, x = data[0], data[1]
    months = data[2:] * 2
    left = 0
    total_days = 0
    total_hugs = 0
    best = 0

    for right in range(2 * n):
        total_days += months[right]
        total_hugs += tri(months[right])

        while total_days > x:
            total_days -= months[left]
            total_hugs -= tri(months[left])
            left += 1

        missing = x - total_days
        value = total_hugs

        if missing and left:
            value += tail(months[left - 1], missing)

        if total_days == x or left:
            best = max(best, value)

    print(best)


# Clause finish_program [Confidence: 0.50]
if __name__ == "__main__":
    main()


