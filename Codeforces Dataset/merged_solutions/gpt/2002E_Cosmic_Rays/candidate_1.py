# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        stack = []
        best = 0
        ans = []

        for _ in range(n):
            a = data[idx]
            b = data[idx + 1]
            idx += 2

            mx = 0
            while stack:
                life, color = stack[-1]
                if color == b:
                    a += life - mx
                    stack.pop()
                elif life <= a:
                    if life > mx:
                        mx = life
                    stack.pop()
                else:
                    break

            stack.append((a, b))
            if a > best:
                best = a
            ans.append(str(best))

        out.append(" ".join(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
