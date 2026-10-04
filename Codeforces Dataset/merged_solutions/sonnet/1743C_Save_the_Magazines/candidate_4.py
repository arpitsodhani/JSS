# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    items = sys.stdin.read().strip().split()
    cases = int(items[0])
    p = 1
    res = []
    for _ in range(cases):
        n = int(items[p])
        p += 1
        s = items[p]
        p += 1
        a = list(map(int, items[p:p + n]))
        p += n

        saved = 0
        block_sum = 0
        block_min = 0
        active = False

        for i in range(n):
            if s[i] == "1":
                if not active:
                    active = True
                    if i > 0 and s[i - 1] == "0":
                        block_sum = a[i - 1] + a[i]
                        block_min = min(a[i - 1], a[i])
                    else:
                        block_sum = a[i]
                        block_min = 0
                else:
                    block_sum += a[i]
                    if block_min and a[i] < block_min:
                        block_min = a[i]
            elif active:
                saved += block_sum - block_min
                active = False

        if active:
            saved += block_sum - block_min

        res.append(str(saved))
    sys.stdout.write("\n".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
