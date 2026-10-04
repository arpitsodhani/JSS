import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause whole_mex [Confidence: 0.80]
def whole_mex(a):
    known = [False] * (len(a) + 2)
    for value in a:
        if value < len(known):
            known[value] = True
    step = 0
    while known[step]:
        step += 1
    return step

# Clause best_mex [Confidence: 1.00]
def best_mex(k, a):
    reach = whole_mex(a)
    return reach if reach < k - 1 else k - 1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, a in read_input():
        out.append(best_mex(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

