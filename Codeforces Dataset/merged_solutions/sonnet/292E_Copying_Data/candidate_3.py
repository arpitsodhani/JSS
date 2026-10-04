# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    i = 0
    n = nums[i]
    m = nums[i + 1]
    i += 2
    a = nums[i:i + n]
    i += n
    b = nums[i:i + n]
    i += n

    length = 1
    while length < n:
        length <<= 1
    times = [0] * (length << 1)
    offsets = [0] * (length << 1)

    def assign(left, right, delta, tm):
        left += length - 1
        right += length - 1
        while left <= right:
            if left & 1:
                times[left] = tm
                offsets[left] = delta
                left += 1
            if not (right & 1):
                times[right] = tm
                offsets[right] = delta
                right -= 1
            left >>= 1
            right >>= 1

    def read(pos):
        node = length + pos - 1
        best_time = 0
        best_delta = 0
        while node:
            if times[node] > best_time:
                best_time = times[node]
                best_delta = offsets[node]
            node >>= 1
        if best_time:
            return a[pos + best_delta - 1]
        return b[pos - 1]

    ans = []
    for tm in range(1, m + 1):
        typ = nums[i]
        i += 1
        if typ == 1:
            x = nums[i]
            y = nums[i + 1]
            k = nums[i + 2]
            i += 3
            assign(y, y + k - 1, x - y, tm)
        else:
            pos = nums[i]
            i += 1
            ans.append(str(read(pos)))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
