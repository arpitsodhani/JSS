# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def dist(a, b):
    d = abs(ord(a) - ord(b))
    return min(d, 26 - d)

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]
    target = 'ACTG'
    ans = 10 ** 9
    for i in range(n - 3):
        cost = 0
        for j in range(4):
            cost += dist(s[i + j], target[j])
        ans = min(ans, cost)
    print(ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
