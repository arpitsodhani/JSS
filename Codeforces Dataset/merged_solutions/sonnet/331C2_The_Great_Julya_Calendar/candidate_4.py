# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    n = int(sys.stdin.readline().strip())
    operations = 0
    while n != 0:
        digits = [ord(c) - 48 for c in str(n)]
        mx = max(digits)
        take = 1
        if mx == 9:
            rev_pos = digits[::-1].index(9)
            scale = 10 ** rev_pos
            take = (n % scale) // 9 + 1
        operations += take
        n -= take * mx

# CLAUSE: finish_program
    sys.stdout.write(f"{operations}\n")

if __name__ == "__main__":
    main()
