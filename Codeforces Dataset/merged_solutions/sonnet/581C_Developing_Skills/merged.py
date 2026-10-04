import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]

# Clause best_rating [Confidence: 0.80]
def best_rating(n, k, skills):
    rating = 0
    steps = []
    for value in skills:
        rating += value // 10
        gap = value % 10
        if gap:
            steps.append(10 - gap)
    steps.sort()
    spent = 0
    for cost in steps:
        if spent + cost > k:
            break
        spent += cost
        rating += 1
    left = k - spent
    room = 10 * n - rating
    extra = left // 10
    if extra > room:
        extra = room
    return rating + extra

# Clause main [Confidence: 1.00]
def main():
    n, k, skills = read_input()
    sys.stdout.write(str(best_rating(n, k, skills)) + "\n")


if __name__ == "__main__":
    main()

