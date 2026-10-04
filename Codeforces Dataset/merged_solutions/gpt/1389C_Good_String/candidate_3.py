# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []

    for s in data[1:1 + t]:
        n = len(s)
        best = 0

        for d in "0123456789":
            best = max(best, s.count(d))

        for a in "0123456789":
            for b in "0123456789":
                if a == b:
                    continue
                need = a
                length = 0
                for ch in s:
                    if ch == need:
                        length += 1
                        need = b if need == a else a
                if length % 2:
                    length -= 1
                best = max(best, length)

        ans.append(str(n - best))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
