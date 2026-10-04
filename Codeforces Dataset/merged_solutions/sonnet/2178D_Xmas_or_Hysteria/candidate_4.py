# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_case(n, m, arr):
    arr.sort(key=lambda item: item[0])

    if n == 1:
        if m == 1:
            return ["0"]
        return ["-1"]

    if m > 0:
        if m * 2 > n:
            return ["-1"]
        pairs = [(arr[i + m][1], arr[i][1]) for i in range(n - m)]
        return [str(len(pairs))] + [str(x) + " " + str(y) for x, y in pairs]

    largest = arr[-1][0]
    below_sum = sum(item[0] for item in arr) - largest
    if below_sum < largest:
        return ["-1"]

    take = 0
    start = n - 2
    while take < largest:
        take += arr[start][0]
        start -= 1
    start += 1

    pairs = []
    left = 0
    while left < start:
        pairs.append((arr[left + 1][1], arr[left][1]))
        left += 1

    boss = arr[-1][1]
    pairs.append((boss, arr[start][1]))

    right = start + 1
    while right < n - 1:
        pairs.append((arr[right][1], boss))
        right += 1

    return [str(len(pairs))] + [str(x) + " " + str(y) for x, y in pairs]

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    answer = []
    for _ in range(values[0]):
        n = values[at]
        m = values[at + 1]
        at += 2
        current = [(values[at + i], i + 1) for i in range(n)]
        at += n
        answer.extend(build_case(n, m, current))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answer))

if __name__ == "__main__":
    main()
