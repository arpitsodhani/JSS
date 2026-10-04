# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    remove = [0] * 26
    count = [0] * 26

    for ch in s:
        count[ord(ch) - 97] += 1

    for i in range(26):
        take = min(k, count[i])
        remove[i] = take
        k -= take
        if k == 0:
            break

    ans = []
    for ch in s:
        idx = ord(ch) - 97
        if remove[idx] > 0:
            remove[idx] -= 1
        else:
            ans.append(ch)

    sys.stdout.write(''.join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
