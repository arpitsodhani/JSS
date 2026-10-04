import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    parent = list(range(n))
    rank = [0] * n
    lang_owner = [-1] * (m + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    idx = 2
    any_language = False

    for employee in range(n):
        k = data[idx]
        idx += 1
        if k:
            any_language = True
        for _ in range(k):
            lang = data[idx]
            idx += 1
            if lang_owner[lang] == -1:
                lang_owner[lang] = employee
            else:
                union(employee, lang_owner[lang])

    if not any_language:
        print(n)
        return

    components = len({find(i) for i in range(n)})
    print(components - 1)

if __name__ == "__main__":
    main()
