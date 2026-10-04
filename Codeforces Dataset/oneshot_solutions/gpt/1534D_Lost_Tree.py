import sys

def ask(v):
    print("?", v, flush=True)
    return list(map(int, sys.stdin.readline().split()))

def main():
    n_line = sys.stdin.readline()
    if not n_line:
        return
    n = int(n_line)

    d1 = ask(1)
    even = [i + 1 for i, d in enumerate(d1) if d % 2 == 0]
    odd = [i + 1 for i, d in enumerate(d1) if d % 2 == 1]

    if len(odd) < len(even):
        query_nodes = odd
    else:
        query_nodes = even

    edges = []
    if 1 in query_nodes:
        for i, d in enumerate(d1, 1):
            if d == 1:
                edges.append((1, i))

    for v in query_nodes:
        if v == 1:
            continue
        d = ask(v)
        for i, x in enumerate(d, 1):
            if x == 1:
                edges.append((v, i))

    print("!", flush=True)
    for u, v in edges:
        print(u, v, flush=True)

if __name__ == "__main__":
    main()
