# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]

    ans = []
    for i in range(n):
        cur = []
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cur.append((a[j], i + 1, j + 1))
        cur.sort(reverse=True)
        for _, u, v in cur:
            ans.append((u, v))

    print(len(ans))
    for u, v in ans:
        print(u, v)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
