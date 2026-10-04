# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    n, d, h = map(int, data)

    if h > d or d > 2 * h or h >= n:
        print(-1)
        return
    if d == 1:
        if n == 2 and h == 1:
            print(1, 2)
        else:
            print(-1)
        return

    edges = []
    cur = 2

    prev = 1
    for _ in range(h):
        edges.append((prev, cur))
        prev = cur
        cur += 1

    if d > h:
        prev = 1
        for _ in range(d - h):
            edges.append((prev, cur))
            prev = cur
            cur += 1

    attach = 2 if d == h else 1
    while cur <= n:
        edges.append((attach, cur))
        cur += 1

    print("\n".join(f"{u} {v}" for u, v in edges))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
