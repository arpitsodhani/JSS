# CLAUSE: setup_environment
import sys

data = sys.stdin.read().strip().split()
n = int(data[0])

# CLAUSE: solve_logic
out = []
if n < 3:
    out.append("No")
else:
    out.append("Yes")
    out.append(f"1 {n}")
    values = []
    for x in range(1, n):
        values.append(str(x))
    out.append(str(n - 1) + " " + " ".join(values))

# CLAUSE: finish_program
sys.stdout.write("\n".join(out))
