# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, r, avg = (data[0], data[1], data[2])
    exams = []
    total = 0
    idx = 3
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        total += a
        exams.append((b, a))
    need = n * avg - total
    if need <= 0:
        print(0)
        return
    exams.sort()
    ans = 0
    for b, a in exams:
        add = min(r - a, need)
        ans += add * b
        need -= add
        if need == 0:
            break
    print(ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
