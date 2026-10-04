# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_answer(n, adj):
    letters = ["b"] * n
    first_gap = None
    for i in range(n):
        if first_gap is not None:
            break
        for j in range(i + 1, n):
            if j not in adj[i]:
                first_gap = (i, j)
                break

    if first_gap is None:
        return letters

    left, right = first_gap
    for v in range(n):
        if v == right or right in adj[v]:
            continue
        letters[v] = "a"
    for v in range(n):
        if v == left or left in adj[v]:
            continue
        if letters[v] == "a":
            return None
        letters[v] = "c"

    for v in range(n):
        if letters[v] == "b":
            if len(adj[v]) != n - 1:
                return None

    return letters

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    adj = [set() for _ in range(n)]
    k = 2
    for _ in range(m):
        u = int(raw[k]) - 1
        v = int(raw[k + 1]) - 1
        k += 2
        adj[u].add(v)
        adj[v].add(u)

    ans = build_answer(n, adj)
    if ans is None:
        sys.stdout.write("No\n")
        return

    for i in range(n):
        for j in range(i + 1, n):
            forbidden = (ans[i] == "a" and ans[j] == "c") or (ans[i] == "c" and ans[j] == "a")
            present = j in adj[i]
            if present == forbidden:
                sys.stdout.write("No\n")
                return

    sys.stdout.write("Yes\n" + "".join(ans) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
