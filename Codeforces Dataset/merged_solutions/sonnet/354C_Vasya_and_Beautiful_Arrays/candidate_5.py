# CLAUSE: setup_environment
import sys

def prefix_counts(numbers, maximum):
    freq = [0] * (maximum + 1)
    for number in numbers:
        freq[number] += 1
    pref = [0] * (maximum + 1)
    for index in range(1, maximum + 1):
        pref[index] = pref[index - 1] + freq[index]
    return pref

# CLAUSE: solve_logic
def has_bad_value(divisor, maximum, pref, k):
    left = divisor + k + 1
    while left <= maximum:
        right = left + divisor - k - 2
        if right > maximum:
            right = maximum
        if right >= left and pref[right] != pref[left - 1]:
            return True
        left += divisor
    return False

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    k = data[1]
    numbers = data[2:]
    maximum = max(numbers)
    minimum = min(numbers)
    pref = prefix_counts(numbers, maximum)
    divisor = minimum
    while divisor:
        if not has_bad_value(divisor, maximum, pref, k):
            print(divisor)
            return
        divisor -= 1

# CLAUSE: finish_program
main()
