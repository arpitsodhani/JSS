# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    p = 0
    n = int(raw[p])
    m = int(raw[p + 1])
    q = int(raw[p + 2])
    p += 3

    table = [0] * (m * 26)

    r = 0
    while r < n:
        s = raw[p]
        p += 1
        bit = 1 << r
        c = 0
        base = 0
        while c < m:
            table[base + s[c] - 97] |= bit
            c += 1
            base += 26
        r += 1

    ans = []
    end = p + q
    while p < end:
        query = raw[p]
        p += 1

        c = 0
        base = 0
        active = table[query[0] - 97]
        if active == 0:
            ans.append("-1")
            continue

        total = 0
        c = 1
        base = 26
        while c < m:
            mask = table[base + query[c] - 97]
            if mask == 0:
                total = -1
                break
            common = active & mask
            if common:
                active = common
            else:
                total += 1
                active = mask
            c += 1
            base += 26

        ans.append(str(total))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
