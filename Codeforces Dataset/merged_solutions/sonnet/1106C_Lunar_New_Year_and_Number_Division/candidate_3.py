# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def pair_score(left, right):
    s = left + right
    return s * s

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    arr = [int(x) for x in data[1:]]
    arr.sort()
    low = 0
    high = n - 1
    answer = 0
    while low < high:
        answer += pair_score(arr[low], arr[high])
        low += 1
        high -= 1
    sys.stdout.write(str(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
