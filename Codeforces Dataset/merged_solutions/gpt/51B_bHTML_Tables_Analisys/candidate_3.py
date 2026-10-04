# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.read().strip()

    ans = []
    stack = []
    i = 0
    n = len(s)

    while i < n:
        if s.startswith("<table>", i):
            ans.append(0)
            stack.append(len(ans) - 1)
            i += 7
        elif s.startswith("</table>", i):
            stack.pop()
            i += 8
        elif s.startswith("<td>", i):
            ans[stack[-1]] += 1
            i += 4
        elif s.startswith("</td>", i):
            i += 5
        elif s.startswith("<tr>", i):
            i += 4
        elif s.startswith("</tr>", i):
            i += 5
        else:
            i += 1

    print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
