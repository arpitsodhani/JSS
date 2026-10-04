# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
t = int(sys.stdin.readline())

digits = []
while t:
    digits.append(t % 6)
    t //= 6
digits.reverse()

ans = set()
curx = 2
cury = 2

def edge(x1, y1, x2, y2):
    ans.add((x1, y1, x2, y2))

def add(bit):
    global curx, cury
    x = curx
    edge(x, x + 2, x, x + 3)
    edge(x + 1, x + 2, x + 1, x + 3)
    edge(x + 2, x, x + 3, x)
    edge(x + 2, x + 1, x + 3, x + 1)
    edge(x - 2, x + 3, x - 1, x + 3)
    edge(x, x + 4, x + 1, x + 4)
    edge(x + 3, x - 2, x + 3, x - 1)
    edge(x + 4, x, x + 4, x + 1)
    edge(x - 1, x + 1, x, x + 1)
    if bit % 3 == 0:
        edge(x - 1, x + 2, x, x + 2)
    if bit % 3 != 2:
        edge(x + 2, x - 1, x + 2, x)
    if bit < 3:
        edge(x + 1, x - 1, x + 1, x)
    curx += 2
    cury += 2

edge(1, 2, 2, 2)
edge(2, 1, 2, 2)

for d in digits:
    add(d)

ans = sorted(e for e in ans if all(1 <= v <= curx for v in e))

out = [f"{curx} {cury}", str(len(ans))]
out.extend(f"{a} {b} {c} {d}" for a, b, c, d in ans)
print("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
