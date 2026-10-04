# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = sys.stdin.read().strip().split()
        n = int(data[0])
        s = data[1]

        if s.count('(') != s.count(')'):
            print(-1)
            return

        ans = 0
        bal = 0
        start = 0
        bad = False

        for i, c in enumerate(s):
            if bal == 0:
                start = i
                bad = False

            if c == '(':
                bal += 1
            else:
                bal -= 1

            if bal < 0:
                bad = True

            if bal == 0 and bad:
                ans += i - start + 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
