# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    n = tokens[ptr]
    m = tokens[ptr + 1]
    ptr += 2
    a = [0] + tokens[ptr:ptr + n]
    ptr += n
    b = [0] + tokens[ptr:ptr + n]
    ptr += n

    base = 1
    while base < n:
        base <<= 1
    latest = [0] * (base << 1)
    origin = [0] * (base << 1)

    def cover(lo, hi, src, now):
        lo += base - 1
        hi += base - 1
        while lo <= hi:
            if lo % 2 == 1:
                latest[lo] = now
                origin[lo] = src
                lo += 1
            if hi % 2 == 0:
                latest[hi] = now
                origin[hi] = src
                hi -= 1
            lo //= 2
            hi //= 2

    def value(pos):
        node = base + pos - 1
        seen = 0
        src_start = 0
        cur = node
        while cur > 0:
            if latest[cur] > seen:
                seen = latest[cur]
                src_start = origin[cur]
            cur //= 2
        if seen == 0:
            return b[pos]
        return a[src_start + pos]

    result = []
    time = 1
    while time <= m:
        typ = tokens[ptr]
        ptr += 1
        if typ == 1:
            x = tokens[ptr]
            y = tokens[ptr + 1]
            k = tokens[ptr + 2]
            ptr += 3
            cover(y, y + k - 1, x - y, time)
        else:
            x = tokens[ptr]
            ptr += 1
            result.append(str(value(x)))
        time += 1

    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
