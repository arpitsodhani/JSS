# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    k = 1
    ans = []
    for _ in range(t):
        n = int(raw[k])
        k += 1
        s = raw[k]
        k += 1
        a = [int(v) for v in raw[k:k + n]]
        k += n

        total = 0
        values = []
        for i, ch in enumerate(s):
            if ch == 49:
                values.append(a[i])
            else:
                if values:
                    total += sum(values) - min(values)
                    values = []
                if i + 1 < n and s[i + 1] == 49:
                    values = [a[i]]

        if values:
            total += sum(values) - min(values)

        ans.append(str(total))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
