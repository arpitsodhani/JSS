# CLAUSE: setup_environment
import sys

def full_month(days):
    return days * (days + 1) // 2

def prefix_month(days, take):
    return take * (take + 1) // 2

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    x = nums[1]
    doubled = nums[2:] * 2

    left = 0
    days = 0
    hugs = 0
    answer = 0

    for right in range(len(doubled)):
        m = doubled[right]
        days += m
        hugs += full_month(m)

        while days > x and left <= right:
            removable = min(doubled[left], days - x)
            days -= removable
            hugs -= prefix_month(doubled[left], removable)
            doubled[left] -= removable
            if doubled[left] == 0:
                left += 1

        if days == x and hugs > answer:
            answer = hugs

    sys.stdout.write(str(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
