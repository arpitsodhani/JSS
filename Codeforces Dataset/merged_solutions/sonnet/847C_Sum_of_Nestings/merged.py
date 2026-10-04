import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause build_sequence [Confidence: 0.80]
def build_sequence(n, k):
    if k > n * (n - 1) // 2:
        return None
    deep = 0
    while (deep + 1) * deep // 2 <= k and deep < n:
        deep += 1
    if deep * (deep - 1) // 2 > k:
        deep -= 1
    rest = k - deep * (deep - 1) // 2
    pieces = ["(" * deep]
    begin = n - deep
    if begin > 0:
        pieces.append(")" * (deep - rest))
        pieces.append("(")
        pieces.append(")" * (rest + 1))
        begin -= 1
        pieces.append("()" * begin)
    else:
        pieces.append(")" * deep)
    return "".join(pieces)

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    answer = build_sequence(n, k)
    sys.stdout.write("Impossible\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()

