# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2

        i = 0
        cnt = 0

        while i < n - 1:
            if s[i] == '(':
                cnt += 1
                i += 2
            else:
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                if j == n:
                    break
                cnt += 1
                i = j + 1

        ans.append(f"{cnt} {n - i}")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
