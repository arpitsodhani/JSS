# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    tests = values[pos]
    pos += 1
    result = []
    for _ in range(tests):
        n = values[pos]
        pos += 1
        arr = values[pos:pos + n]
        pos += n
        total = sum(arr)
        left = 0
        answer = 0
        for i in range(n - 1):
            left += arr[i]
            current = gcd(left, total - left)
            if current > answer:
                answer = current
        result.append(str(answer))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
