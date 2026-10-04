# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def best_saved(n, s, a):
    ans = 0
    start = 0
    while start < n:
        while start < n and s[start] == "0":
            start += 1
        if start == n:
            break
        end = start
        total = 0
        low = 10 ** 30
        if start > 0 and s[start - 1] == "0":
            total += a[start - 1]
            low = a[start - 1]
        while end < n and s[end] == "1":
            total += a[end]
            low = min(low, a[end])
            end += 1
        if start > 0 and s[start - 1] == "0":
            ans += total - low
        else:
            ans += total
        start = end
    return ans

def main():
    tokens = sys.stdin.buffer.read().split()
    q = int(tokens[0])
    at = 1
    answers = []
    for _ in range(q):
        n = int(tokens[at])
        at += 1
        s = tokens[at].decode()
        at += 1
        arr = [int(x) for x in tokens[at:at + n]]
        at += n
        answers.append(str(best_saved(n, s, arr)))
    print("\n".join(answers))

# CLAUSE: finish_program
main()
