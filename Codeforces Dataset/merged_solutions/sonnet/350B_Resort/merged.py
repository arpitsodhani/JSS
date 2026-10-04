import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    kind = data[1:1 + n]
    source = data[1 + n:1 + 2 * n]
    return n, kind, source

# Clause longest_path [Confidence: 0.80]
def longest_path(n, kind, source):
    outdeg = [0] * (n + 1)
    for v in range(1, n + 1):
        u = source[v - 1]
        if u:
            outdeg[u] += 1
    best = []
    for v in range(1, n + 1):
        if kind[v - 1] != 1:
            continue
        chain = [v]
        u = source[v - 1]
        while u and kind[u - 1] == 0 and outdeg[u] == 1:
            chain.append(u)
            u = source[u - 1]
        if len(chain) > len(best):
            chain.reverse()
            best = chain
    return best

# Clause main [Confidence: 1.00]
def main():
    n, kind, source = read_input()
    path = longest_path(n, kind, source)
    sys.stdout.write(str(len(path)) + "\n" + " ".join(map(str, path)) + "\n")


if __name__ == "__main__":
    main()

