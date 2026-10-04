import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        s = data[i]
        if len(set(s)) == 1:
            ans.append("-1")
        else:
            ans.append("".join(sorted(s)))
    print("\n".join(ans))

if __name__ == "__main__":
    main()
