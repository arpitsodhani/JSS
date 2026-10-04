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
            seen = {0}
            pref = 0
            ok = False

            for i in range(1, n + 1):
                x = data[idx]
                idx += 1
                if i % 2:
                    pref += x
                else:
                    pref -= x

                if pref in seen:
                    ok = True
                seen.add(pref)

            ans.append("YES" if ok else "NO")

        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
