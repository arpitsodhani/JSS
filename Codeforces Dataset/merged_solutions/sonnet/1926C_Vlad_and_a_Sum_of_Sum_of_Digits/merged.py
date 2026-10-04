# Clause setup_environment [Confidence: 0.40]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    nums = data[1:1 + t]
    limit = max(nums) if nums else 0
    pref = [0] * (limit + 1)
    for i in range(1, limit + 1):
        pref[i] = pref[i - 1] + digit_sum(i)
    sys.stdout.write("\n".join(str(pref[n]) for n in nums))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


