import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for idx in range(1, t + 1):
        n = int(data[idx])
        k = (n + 1) // 2
        out.append(str(k))
        for i in range(1, k + 1):
            out.append(f"{3 * i - 1} {3 * (n - i + 1)}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
