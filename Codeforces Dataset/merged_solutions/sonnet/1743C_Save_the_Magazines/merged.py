# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        s = data[pos]
        pos += 1
        a = list(map(int, data[pos:pos + n]))
        pos += n

        ans = 0
        i = 0
        while i < n:
            if s[i] == "0":
                if i + 1 < n and s[i + 1] == "1":
                    total = a[i]
                    smallest = a[i]
                    i += 1
                    while i < n and s[i] == "1":
                        total += a[i]
                        if a[i] < smallest:
                            smallest = a[i]
                        i += 1
                    ans += total - smallest
                else:
                    i += 1
            else:
                total = 0
                while i < n and s[i] == "1":
                    total += a[i]
                    i += 1
                ans += total
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


