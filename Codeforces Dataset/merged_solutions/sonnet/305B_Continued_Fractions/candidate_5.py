# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    p = next(stream)
    q = next(stream)
    n = next(stream)
    terms = [next(stream) for _ in range(n)]

    ok = True
    for i in range(n):
        if q == 0:
            ok = False
            break

        quotient, p = divmod(p, q)
        if quotient != terms[i]:
            ok = False
            break

        if i + 1 == n:
            ok = p == 0
            break

        if p == 0:
            ok = False
            break

        p, q = q, p

    sys.stdout.write("YES" if ok else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
