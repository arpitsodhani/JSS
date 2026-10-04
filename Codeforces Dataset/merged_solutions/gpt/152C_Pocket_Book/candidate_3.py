# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import re

    MOD = 1000000007

    data = sys.stdin.read()
    match = re.match(r"\s*(\d+)\s+(\d+)", data)
    n = int(match.group(1))
    m = int(match.group(2))

    letters = re.findall(r"[A-Za-z]", data[match.end():])
    ans = 1

    for col in range(m):
        seen = set()
        for row in range(n):
            seen.add(letters[row * m + col])
        ans = (ans * len(seen)) % MOD

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
