import sys
MOD = 10 ** 9 + 7

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause total_scalar [Confidence: 1.00]
def total_scalar(n, a):
    order = sorted(range(n), key=lambda i: a[i])
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    total = 0
    for index in order:
        position = index + 1
        weight = position * (n - position + 1)
        smaller_left = 0
        spot = position - 1
        while spot > 0:
            smaller_left += left[spot]
            spot -= spot & -spot
        smaller_right = 0
        spot = n - position
        while spot > 0:
            smaller_right += right[spot]
            spot -= spot & -spot
        weight += (n - position + 1) * smaller_left
        weight += position * smaller_right
        total = (total + a[index] * weight) % MOD
        spot = position
        while spot <= n:
            left[spot] += position
            spot += spot & -spot
        spot = n - position + 1
        while spot <= n:
            right[spot] += n - position + 1
            spot += spot & -spot
    return total % MOD

# Clause main [Confidence: 1.00]
def main():
    n, a = read_input()
    sys.stdout.write(str(total_scalar(n, a)) + "\n")


if __name__ == "__main__":
    main()

