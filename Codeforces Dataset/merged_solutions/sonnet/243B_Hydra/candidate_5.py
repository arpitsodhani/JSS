# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    it = iter(raw)
    n = int(next(it))
    m = int(next(it))
    h = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(n + 1)]
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    state = [0] * (n + 1)
    clock = 100

    def build(u, v):
        nonlocal clock

        du = len(adj[u])
        dv = len(adj[v])
        if du - 1 < h or dv - 1 < t or du + dv - 2 < h + t:
            return None

        clock += 2
        left = clock
        shared = clock + 1

        for node in adj[u]:
            if node != v:
                state[node] = left

        right_only = []
        both = []

        for node in adj[v]:
            if node == u:
                continue
            if state[node] == left:
                state[node] = shared
                both.append(node)
            else:
                right_only.append(node)

        left_only = []
        for node in adj[u]:
            if node != v and state[node] == left:
                left_only.append(node)

        left_gap = max(0, h - len(left_only))
        right_gap = max(0, t - len(right_only))

        if left_gap + right_gap > len(both):
            return None

        left_answer = []
        right_answer = []

        for node in left_only:
            if len(left_answer) == h:
                break
            left_answer.append(node)

        for i in range(left_gap):
            left_answer.append(both[i])

        for node in right_only:
            if len(right_answer) == t:
                break
            right_answer.append(node)

        for i in range(left_gap, left_gap + right_gap):
            right_answer.append(both[i])

        return left_answer, right_answer

    answer = None
    for u, v in edges:
        answer = build(u, v)
        if answer is not None:
            a, b = u, v
            break
        answer = build(v, u)
        if answer is not None:
            a, b = v, u
            break

    if answer is None:
        sys.stdout.write("NO\n")
        return

    heads, tails = answer
    lines = ["YES", str(a) + " " + str(b), " ".join(map(str, heads)), " ".join(map(str, tails))]
    sys.stdout.write("\n".join(lines) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
