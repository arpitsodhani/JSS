# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def solve_case(n, arr):
    parent = list(range(n))
    size = [1] * n
    answer = []

    for mod in range(n - 1, 0, -1):
        first = {}
        chosen = None

        for i, value in enumerate(arr):
            rem = value % mod
            if rem in first:
                j = first[rem]
                ri = find(parent, i)
                rj = find(parent, j)
                if ri != rj:
                    if size[ri] < size[rj]:
                        ri, rj = rj, ri
                    parent[rj] = ri
                    size[ri] += size[rj]
                    chosen = (i + 1, j + 1)
                    break
            else:
                first[rem] = i

        if chosen is None:
            return None
        answer.append(chosen)

    answer.reverse()
    return answer

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    lines = []

    for _ in range(t):
        n = data[p]
        p += 1
        arr = data[p:p + n]
        p += n
        edges = solve_case(n, arr)

        if edges is None:
            lines.append("NO")
        else:
            lines.append("YES")
            lines.extend(str(u) + " " + str(v) for u, v in edges)

    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
