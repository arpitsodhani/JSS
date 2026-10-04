# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = sys.stdin.read().strip().split()
        if not data:
            return

        n = int(data[0])
        s = data[1].strip()
        digits = [int(c) for c in s]
        total = sum(digits)

        for target in range(1, total + 1):
            cur = 0
            parts = 0
            ok = True

            for d in digits:
                cur += d
                if cur == target:
                    parts += 1
                    cur = 0
                elif cur > target:
                    ok = False
                    break

            if ok and cur == 0 and parts >= 2:
                print("YES")
                return

        if total == 0 and n >= 2:
            print("YES")
        else:
            print("NO")

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
