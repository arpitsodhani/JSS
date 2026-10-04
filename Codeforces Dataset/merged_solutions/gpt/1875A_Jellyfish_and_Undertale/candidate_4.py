# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        n = data[idx + 2]
        idx += 3

        total = b
        limit = a - 1
        for i in range(n):
            total += min(data[idx + i], limit)
        idx += n

        ans.append(str(total))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
