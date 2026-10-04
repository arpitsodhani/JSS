# CLAUSE: setup_environment
import sys

def digit_sum(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    nums = data[1:1 + t]
    limit = max(nums) if nums else 0
    pref = [0] * (limit + 1)
    for i in range(1, limit + 1):
        pref[i] = pref[i - 1] + digit_sum(i)
    sys.stdout.write("\n".join(str(pref[n]) for n in nums))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
