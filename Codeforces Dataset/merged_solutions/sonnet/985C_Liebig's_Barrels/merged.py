import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    l = data[2]
    staves = sorted(data[3:3 + n * k])
    return n, k, l, staves

# Clause count_usable [Confidence: 1.00]
def count_usable(staves, l):
    limit = staves[0] + l
    usable = 0
    for v in staves:
        if v > limit:
            break
        usable += 1
    return usable

# Clause compute_answer [Confidence: 1.00]
def compute_answer(n, k, staves, usable):
    if usable < n:
        return 0
    ans = 0
    pos = 0
    for barrel in range(n):
        ans += staves[pos]
        remaining = n - barrel - 1
        pos += min(k, usable - pos - remaining)
    return ans

# Clause main [Confidence: 1.00]
def main():
    n, k, l, staves = read_input()
    usable = count_usable(staves, l)
    print(compute_answer(n, k, staves, usable))


if __name__ == "__main__":
    main()

