# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    a = [int(x) for x in raw[1:]]

    order = sorted(range(n), key=a.__getitem__)
    active = [0] * n
    parent = [-1] * n
    size = [0] * n
    odd_blocks = 0

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def join(u, v):
        nonlocal odd_blocks
        ru = root(u)
        rv = root(v)
        if ru == rv:
            return
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        odd_blocks -= size[ru] % 2
        odd_blocks -= size[rv] % 2
        parent[rv] = ru
        size[ru] += size[rv]
        odd_blocks += size[ru] % 2

    i = 0
    answer = "YES"
    while i < n:
        j = i
        h = a[order[i]]
        while j < n and a[order[j]] == h:
            p = order[j]
            active[p] = 1
            parent[p] = p
            size[p] = 1
            odd_blocks += 1
            if p > 0 and active[p - 1]:
                join(p, p - 1)
            if p + 1 < n and active[p + 1]:
                join(p, p + 1)
            j += 1
        if j < n and odd_blocks:
            answer = "NO"
            break
        i = j

    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
