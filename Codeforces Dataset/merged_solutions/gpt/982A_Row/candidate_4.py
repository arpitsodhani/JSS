# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().strip().split()

    if len(data) >= 2:
        n = int(data[0])
        s = data[1]
    else:
        t = data[0]
        n = None
        s = ""
        for i in range(1, len(t) + 1):
            if int(t[:i]) == len(t) - i:
                n = int(t[:i])
                s = t[i:]
                break

    ok = True

    if "11" in s:
        ok = False
    if n == 1:
        if s == "0":
            ok = False
    else:
        if s[0] == "0" and s[1] == "0":
            ok = False
        if s[-1] == "0" and s[-2] == "0":
            ok = False
        if "000" in s:
            ok = False

    print("Yes" if ok else "No")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
