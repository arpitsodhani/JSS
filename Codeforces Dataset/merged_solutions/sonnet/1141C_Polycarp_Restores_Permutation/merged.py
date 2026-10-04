import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]

# Clause restore [Confidence: 1.00]
def restore(n, q):
    walk = [0]
    here = 0
    for step in q:
        here += step
        walk.append(here)
    shift = 1 - min(walk)
    p = [entry + shift for entry in walk]
    marked = [False] * (n + 1)
    for entry in p:
        if entry < 1 or entry > n or marked[entry]:
            return None
        marked[entry] = True
    return p

# Clause main [Confidence: 1.00]
def main():
    n, q = read_input()
    p = restore(n, q)
    if p is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, p)) + "\n")


if __name__ == "__main__":
    main()

