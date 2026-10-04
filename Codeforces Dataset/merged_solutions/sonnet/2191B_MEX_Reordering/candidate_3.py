# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def possible(a):
    n = len(a)
    counts = Counter(a)
    mex = 0
    while counts.get(mex, 0):
        mex += 1
    if mex == 0:
        return n == 1
    for value in range(mex):
        if counts[value] == 1:
            return True
    return False

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        a = [int(x) for x in data[pos:pos + n]]
        pos += n
        out.append("YES" if possible(a) else "NO")
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
