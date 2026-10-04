# CLAUSE: setup_environment
import sys

def ask(x, y):
    print(1, x, y, flush=True)
    return sys.stdin.readline().strip() == "TAK"

# CLAUSE: solve_logic
def locate(left, right):
    while left < right:
        middle = (left + right) // 2
        if ask(middle, middle + 1):
            right = middle
        else:
            left = middle + 1
    return left

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    n, k = map(int, data)
    first = locate(1, n)
    second = -1
    if first > 1:
        option = locate(1, first - 1)
        if ask(option, first):
            second = option
    if second == -1 and first < n:
        second = locate(first + 1, n)
    print(2, first, second, flush=True)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
