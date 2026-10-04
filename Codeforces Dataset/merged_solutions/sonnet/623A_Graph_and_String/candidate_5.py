# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def possible_pair(x, y, mat):
    if x == y:
        return True
    return not ((x == "a" and y == "c") or (x == "c" and y == "a"))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        mat[i][i] = 1

    at = 2
    for _ in range(m):
        u = data[at] - 1
        v = data[at + 1] - 1
        at += 2
        mat[u][v] = 1
        mat[v][u] = 1

    miss_count = [0] * n
    for i in range(n):
        row = mat[i]
        count = 0
        for j in range(n):
            if i != j and row[j] == 0:
                count += 1
        miss_count[i] = count

    ans = ["b"] * n
    for s in range(n):
        if miss_count[s] == 0 or ans[s] != "b":
            continue
        ans[s] = "a"
        frontier = [s]
        while frontier:
            v = frontier.pop()
            next_letter = "c" if ans[v] == "a" else "a"
            for u in range(n):
                if u != v and mat[v][u] == 0:
                    if ans[u] == "b":
                        ans[u] = next_letter
                        frontier.append(u)
                    elif ans[u] != next_letter:
                        sys.stdout.write("No\n")
                        return

    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j] != possible_pair(ans[i], ans[j], mat):
                sys.stdout.write("No\n")
                return

    sys.stdout.write("Yes\n" + "".join(ans) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
