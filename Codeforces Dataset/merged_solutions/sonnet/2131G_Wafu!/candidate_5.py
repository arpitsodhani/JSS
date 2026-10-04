# CLAUSE: setup_environment
import sys

MOD = 10**9 + 7

# CLAUSE: solve_logic
def answer(k, items):
    exists = set(items)
    score = 1
    for _ in range(k):
        if not exists:
            break
        m = min(exists)
        exists.remove(m)
        score = score * m % MOD
        exists.update(range(1, m))
    return score

def main():
    a = list(map(int, sys.stdin.buffer.read().split()))
    idx = 1
    res = []
    for _ in range(a[0]):
        n = a[idx]
        k = a[idx + 1]
        idx += 2
        res.append(str(answer(k, a[idx:idx + n])))
        idx += n
    sys.stdout.write("\n".join(res))

# CLAUSE: finish_program
main()
