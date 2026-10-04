# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    if not numbers:
        return
    n = numbers[0]
    arr = numbers[1:]
    half = n // 2
    ans = -1
    for i in range(half):
        if arr[i] == arr[i + half]:
            ans = i + 1
            break

# CLAUSE: finish_program
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()
