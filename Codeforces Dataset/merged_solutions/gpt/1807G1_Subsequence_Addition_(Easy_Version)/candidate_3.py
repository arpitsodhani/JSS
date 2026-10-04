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
            c = data[idx:idx + n]
            idx += n
            c.sort()

            if c[0] != 1:
                ans.append("NO")
                continue

            s = 1
            ok = True
            for x in c[1:]:
                if x > s:
                    ok = False
                    break
                s += x

            ans.append("YES" if ok else "NO")

        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
