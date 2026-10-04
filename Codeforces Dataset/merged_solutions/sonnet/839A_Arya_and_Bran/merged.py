import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]

# Clause last_day [Confidence: 1.00]
def last_day(k, a):
    saved = 0
    given = 0
    for i in range(len(a)):
        saved += a[i]
        hand = 8 if saved > 8 else saved
        saved -= hand
        given += hand
        if given >= k:
            return i + 1
    return -1

# Clause main [Confidence: 1.00]
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % last_day(k, a))


if __name__ == "__main__":
    main()

