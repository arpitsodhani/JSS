# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = list(data[2])

    i = 0
    while i + 1 < n and not (s[i] == '4' and s[i + 1] == '7'):
        i += 1

    while k > 0 and i + 1 < n:
        if i % 2 == 0:
            s[i + 1] = '4'
            k -= 1
            if k > 0 and i + 2 < n and s[i + 2] == '7':
                if k % 2 == 1:
                    s[i + 1] = '7'
                break
            i += 1
        else:
            if i > 0 and s[i - 1] == '4':
                if k % 2 == 1:
                    s[i] = '7'
                break
            s[i] = '7'
            k -= 1
            i += 1

        while i + 1 < n and not (s[i] == '4' and s[i + 1] == '7'):
            i += 1

    print(''.join(s))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
