# CLAUSE: setup_environment
import sys

def read_words(values, count):
    at = 2
    result = []
    for _ in range(count):
        size = values[at]
        at += 1
        result.append(values[at:at + size])
        at += size
    return result

# CLAUSE: solve_logic
def first_bad_interval(a, b, c):
    limit = min(len(a), len(b))
    pos = 0
    while pos < limit and a[pos] == b[pos]:
        pos += 1
    if pos == limit:
        if len(a) > len(b):
            return None
        return ()
    x = a[pos] - 1
    y = b[pos] - 1
    if x < y:
        return ((c - y, c - x - 1),)
    return ((0, c - x - 1), (c - y, c - 1))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, c = data[0], data[1]
    words = read_words(data, n)
    diff = [0] * (c + 1)
    for i in range(n - 1):
        intervals = first_bad_interval(words[i], words[i + 1], c)
        if intervals is None:
            sys.stdout.write("-1")
            return
        for left, right in intervals:
            if left <= right:
                diff[left] += 1
                diff[right + 1] -= 1
    active = 0
    for shift in range(c):
        active += diff[shift]
        if active == 0:
            sys.stdout.write(str(shift))
            return
    sys.stdout.write("-1")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
