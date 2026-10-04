# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    n = int(sys.stdin.readline())
    ans = 0
    while n:
        text = str(n)
        digit = max(map(int, text))
        if digit == 9:
            idx = text.rfind("9")
            tail_len = len(text) - idx - 1
            unit = 10 ** tail_len
            steps = (n % unit) // 9 + 1
        else:
            steps = 1
        n -= digit * steps
        ans += steps

# CLAUSE: finish_program
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()
