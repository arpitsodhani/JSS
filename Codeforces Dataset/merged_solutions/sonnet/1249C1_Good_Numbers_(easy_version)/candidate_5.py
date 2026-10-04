# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def next_good(n):
    ternary = []
    x = n
    while x > 0:
        ternary.append(x % 3)
        x //= 3
    if not ternary:
        ternary.append(0)

    need_raise = False
    prefix = []
    for digit in reversed(ternary):
        if need_raise:
            prefix.append(0)
        elif digit == 2:
            need_raise = True
            prefix.append(0)
        else:
            prefix.append(digit)

    if not need_raise:
        return n

    carry = 1
    for i in range(len(prefix) - 1, -1, -1):
        if carry == 0:
            break
        if prefix[i] == 0:
            prefix[i] = 1
            carry = 0
        else:
            prefix[i] = 0

    if carry:
        prefix.insert(0, 1)

    answer = 0
    for digit in prefix:
        answer = answer * 3 + digit
    return answer

def main():
    data = sys.stdin.read().strip().split()
    q = int(data[0])
    print("\n".join(str(next_good(int(data[i]))) for i in range(1, q + 1)))

# CLAUSE: finish_program
main()
