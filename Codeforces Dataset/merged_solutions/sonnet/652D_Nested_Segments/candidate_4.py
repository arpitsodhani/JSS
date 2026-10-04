# CLAUSE: setup_environment
import sys

def add(tree, n, at):
    while at <= n:
        tree[at] += 1
        at += at & -at

def count_before(tree, at):
    ans = 0
    while at > 0:
        ans += tree[at]
        at &= at - 1
    return ans

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    segments = []
    rights = [0] * n
    j = 1
    for idx in range(n):
        left = int(raw[j])
        right = int(raw[j + 1])
        j += 2
        segments.append([left, right, idx])
        rights[idx] = right

    order = sorted(range(n), key=lambda x: segments[x][0], reverse=True)
    by_right = {right: pos for pos, right in enumerate(sorted(rights), 1)}
    tree = [0] * (n + 1)
    out = [0] * n

    for sidx in order:
        right = segments[sidx][1]
        pos = by_right[right]
        out[segments[sidx][2]] = count_before(tree, pos - 1)
        add(tree, n, pos)

    sys.stdout.write("\n".join(map(str, out)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
