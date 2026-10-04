# Clause setup_environment [Confidence: 0.40]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    c = nums[1]
    ptr = 2
    diff = [0] * (c + 1)
    previous = None

    for index in range(n):
        length = nums[ptr]
        ptr += 1
        current = nums[ptr:ptr + length]
        ptr += length

        if previous is not None:
            p = 0
            border = len(previous) if len(previous) < len(current) else len(current)
            while p < border and previous[p] == current[p]:
                p += 1

            if p == border:
                if len(previous) > len(current):
                    sys.stdout.write("-1")
                    return
            else:
                first = previous[p] - 1
                second = current[p] - 1
                if first < second:
                    left = c - second
                    right = c - first - 1
                    diff[left] += 1
                    diff[right + 1] -= 1
                else:
                    stop = c - first
                    start = c - second
                    if stop:
                        diff[0] += 1
                        diff[stop] -= 1
                    if start < c:
                        diff[start] += 1
                        diff[c] -= 1

        previous = current

    running = 0
    answer = -1
    shift = 0
    while shift < c:
        running += diff[shift]
        if running == 0:
            answer = shift
            break
        shift += 1
    sys.stdout.write(str(answer))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


