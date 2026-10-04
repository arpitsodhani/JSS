import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause split_message [Confidence: 0.80]
def split_message(t):
    n = len(t)
    for extent in range(n // 2 + 1, n):
        if 2 * extent - n <= 0:
            continue
        if t[:extent] == t[n - extent:]:
            return t[:extent]
    return None

# Clause main [Confidence: 1.00]
def main():
    t = read_input()
    answer = split_message(t)
    if answer is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % answer)


if __name__ == "__main__":
    main()

