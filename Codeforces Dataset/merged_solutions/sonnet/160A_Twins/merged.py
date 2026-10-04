import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause fewest_coins [Confidence: 1.00]
def fewest_coins(a):
    arranged = sorted(a, reverse=True)
    total = sum(a)
    mine = 0
    taken = 0
    for entry in arranged:
        if mine * 2 > total:
            break
        mine += entry
        taken += 1
    return taken

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % fewest_coins(read_input()))


if __name__ == "__main__":
    main()

