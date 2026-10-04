# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return

    n = nums[0]
    f = [0] + nums[1:n + 1]
    state = [0] * (n + 1)
    comp = [0] * (n + 1)
    reps = []

    for start in range(1, n + 1):
        if state[start]:
            continue

        path = []
        pos = {}
        v = start
        while state[v] == 0:
            state[v] = 1
            pos[v] = len(path)
            path.append(v)
            v = f[v]

        if state[v] == 1 and v in pos:
            reps.append(v)
            cid = len(reps)
            for u in path[pos[v]:]:
                comp[u] = cid

        for u in path:
            state[u] = 2

    for v in range(1, n + 1):
        if comp[v] == 0:
            reps.append(v)
            comp[v] = len(reps)

    cnum = len(reps)
    if cnum == 1:
        print(0)
        return

    in_count = [0] * (cnum + 1)
    out_count = [0] * (cnum + 1)

    for v in range(1, n + 1):
        left = comp[v]
        right = comp[f[v]]
        if left != right:
            out_count[left] += 1
            in_count[right] += 1

    starts = []
    ends = []
    for c in range(1, cnum + 1):
        if in_count[c] == 0:
            starts.append(c)
        if out_count[c] == 0:
            ends.append(c)

    amount = max(len(starts), len(ends))
    out = [str(amount)]
    a = len(ends)
    b = len(starts)
    for i in range(amount):
        out.append(str(reps[ends[i % a] - 1]) + " " + str(reps[starts[(i + 1) % b] - 1]))

    print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
