import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return data[1:1 + n], data[1 + n:1 + 2 * n]

# Clause best_team [Confidence: 0.80]
def best_team(top, low):
    took_top = 0
    took_low = 0
    took_none = 0
    for i in range(len(top)):
        best_other = took_low if took_low > took_none else took_none
        fresh_top = best_other + top[i]
        best_other = took_top if took_top > took_none else took_none
        fresh_low = best_other + low[i]
        fresh_none = took_none
        if took_top > fresh_none:
            fresh_none = took_top
        if took_low > fresh_none:
            fresh_none = took_low
        took_top = fresh_top
        took_low = fresh_low
        took_none = fresh_none
    best = took_top
    if took_low > best:
        best = took_low
    if took_none > best:
        best = took_none
    return best

# Clause main [Confidence: 1.00]
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % best_team(top, low))


if __name__ == "__main__":
    main()

