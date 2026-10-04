# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_all(data):
    it = iter(data)
    tests = int(next(it))
    res = []
    for _ in range(tests):
        n = int(next(it))
        pref = 0
        entries = []
        for idx in range(n):
            entries.append([pref, idx])
            pref += int(next(it))
        entries.sort()
        perm = [0] * n
        for value, entry in zip(range(n, 0, -1), entries):
            perm[entry[1]] = value
        res.append(" ".join(map(str, perm)))
    return res

def main():
    sys.stdout.write("\n".join(solve_all(sys.stdin.buffer.read().split())))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
