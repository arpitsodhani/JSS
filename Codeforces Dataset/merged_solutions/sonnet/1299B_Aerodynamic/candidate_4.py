# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    xs = [0] * n
    ys = [0] * n
    k = 1
    for i in range(n):
        xs[i] = int(raw[k])
        ys[i] = int(raw[k + 1])
        k += 2

    answer = "YES"
    if n % 2 != 0:
        answer = "NO"
    else:
        half = n // 2
        sx = xs[0] + xs[half]
        sy = ys[0] + ys[half]
        i = 1
        while i < half:
            if xs[i] + xs[i + half] != sx or ys[i] + ys[i + half] != sy:
                answer = "NO"
                break
            i += 1

    sys.stdout.write(answer)

# CLAUSE: finish_program
main()
