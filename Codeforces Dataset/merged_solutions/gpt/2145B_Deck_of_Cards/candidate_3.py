# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = sys.stdin.read().split()
        t = int(data[0])
        idx = 1
        out = []
        for _ in range(t):
            n = int(data[idx])
            k = int(data[idx + 1])
            s = data[idx + 2]
            idx += 3

            a = s.count('0')
            b = s.count('1')
            c = s.count('2')

            ans = ['+'] * n
            for i in range(n):
                if i < a + c or i >= n - b - c:
                    ans[i] = '?'
                if i < a or i >= n - b or k == n:
                    ans[i] = '-'
            out.append(''.join(ans))

        sys.stdout.write('\n'.join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
