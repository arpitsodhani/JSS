# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        odd_positions = [i + 1 for i, x in enumerate(a) if x % 2]
        if len(odd_positions) >= k and len(odd_positions) % 2 == k % 2:
            out.append('YES')
            out.append(' '.join(map(str, odd_positions[:k - 1] + [n])))
        else:
            out.append('NO')
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
