import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    parts = sys.stdin.readline().split()
    return int(parts[0]), int(parts[1])

# Clause ask [Confidence: 1.00]
def ask(y):
    sys.stdout.write("%d\n" % y)
    sys.stdout.flush()
    return int(sys.stdin.readline())

# Clause learn_pattern [Confidence: 1.00]
def learn_pattern(n):
    honest = []
    for _ in range(n):
        answer = ask(1)
        if answer == 0:
            return None
        honest.append(1 if answer == 1 else 0)
    return honest

# Clause hunt [Confidence: 1.00]
def hunt(m, honest):
    n = len(honest)
    advance = n
    bottom = 2
    high = m
    while bottom <= high:
        mid = (bottom + high) // 2
        verdict = ask(mid)
        if verdict == 0:
            return
        truth = verdict if honest[advance % n] else -verdict
        advance += 1
        if truth == 1:
            bottom = mid + 1
        else:
            high = mid - 1

# Clause main [Confidence: 1.00]
def main():
    m, n = read_input()
    honest = learn_pattern(n)
    if honest is not None:
        hunt(m, honest)


if __name__ == "__main__":
    main()

