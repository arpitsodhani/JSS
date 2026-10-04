# CLAUSE: setup_environment
import sys

def touches(lo1, hi1, lo2, hi2):
    return lo1 <= hi2 + 1 and lo2 <= hi1 + 1

# CLAUSE: solve_logic
def answer_for(arr):
    n = len(arr)
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) <= 1:
            return 0
    best = n
    for cut in range(n - 1):
        lmin = lmax = arr[cut]
        for left in range(cut, -1, -1):
            v = arr[left]
            if v < lmin:
                lmin = v
            if v > lmax:
                lmax = v
            rmin = rmax = arr[cut + 1]
            for right in range(cut + 1, n):
                w = arr[right]
                if w < rmin:
                    rmin = w
                if w > rmax:
                    rmax = w
                if touches(lmin, lmax, rmin, rmax):
                    cost = right - left - 1
                    if cost < best:
                        best = cost
                    break
    if best == n:
        return -1
    return best

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    pos = 1
    out = []
    for _ in range(nums[0]):
        n = nums[pos]
        pos += 1
        arr = nums[pos:pos + n]
        pos += n
        out.append(str(answer_for(arr)))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
