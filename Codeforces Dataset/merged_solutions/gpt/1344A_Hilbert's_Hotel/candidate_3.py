# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            seen = [False] * n

            ok = True
            for i in range(n):
                a = data[idx + i]
                r = (i + a) % n
                if seen[r]:
                    ok = False
                seen[r] = True

            idx += n
            ans.append("YES" if ok else "NO")

        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
