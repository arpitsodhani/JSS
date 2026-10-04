# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def next_good(n):
        digits = []
        x = n
        while x:
            digits.append(x % 3)
            x //= 3
        digits.append(0)

        pos = -1
        for i, d in enumerate(digits):
            if d == 2:
                pos = i

        if pos == -1:
            return n

        carry = pos + 1
        while digits[carry] == 2:
            carry += 1
        digits[carry] += 1

        for i in range(carry):
            digits[i] = 0

        for i in range(carry + 1, len(digits)):
            if digits[i] == 2:
                return next_good(sum(d * (3 ** j) for j, d in enumerate(digits)))

        ans = 0
        p = 1
        for d in digits:
            ans += d * p
            p *= 3
        return ans

    data = list(map(int, sys.stdin.read().split()))
    q = data[0]
    out = []
    for n in data[1:1 + q]:
        out.append(str(next_good(n)))
    print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
