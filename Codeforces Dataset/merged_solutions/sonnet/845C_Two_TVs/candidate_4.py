# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    marks = {}
    k = 1
    for _ in range(n):
        l = nums[k]
        r = nums[k + 1]
        k += 2
        current = marks.get(l)
        if current is None:
            marks[l] = [1, 0]
        else:
            current[0] += 1
        current = marks.get(r)
        if current is None:
            marks[r] = [0, 1]
        else:
            current[1] += 1
    active = 0
    for point in sorted(marks):
        active += marks[point][0]
        if active > 2:
            sys.stdout.write("NO")
            return
        active -= marks[point][1]
    sys.stdout.write("YES")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
