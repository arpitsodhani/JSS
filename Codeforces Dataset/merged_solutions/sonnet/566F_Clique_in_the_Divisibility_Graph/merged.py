import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause longest_chain [Confidence: 1.00]
def longest_chain(a):
    top = a[-1]
    chain = [0] * (top + 1)
    best = 0
    for item in a:
        here = chain[item] + 1
        if here > best:
            best = here
        advance = item + item
        while advance <= top:
            if here > chain[advance]:
                chain[advance] = here
            advance += item
    return best

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % longest_chain(read_input()))


if __name__ == "__main__":
    main()

