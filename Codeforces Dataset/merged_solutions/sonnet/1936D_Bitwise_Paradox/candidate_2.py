# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    n = int(data[p])
    p += 1
    q = int(data[p])
    p += 1
    v = int(data[p])
    p += 1
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[p])
        p += 1
    for i in range(1, n + 1):
        b[i] = int(data[p])
        p += 1
    ans = []
    for _ in range(q):
        t = int(data[p])
        p += 1
        if t == 1:
            i = int(data[p])
            x = int(data[p + 1])
            p += 2
            b[i] = x
        else:
            l = int(data[p])
            r = int(data[p + 1])
            p += 2
            best = None
            for left in range(l, r + 1):
                current_or = 0
                current_max = 0
                for right in range(left, r + 1):
                    current_or |= b[right]
                    if a[right] > current_max:
                        current_max = a[right]
                    if current_or >= v:
                        if best is None or current_max < best:
                            best = current_max
                        break
            ans.append(str(best if best is not None else -1))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
