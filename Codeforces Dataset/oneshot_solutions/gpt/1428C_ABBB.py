import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        s = data[i]
        stack = []
        for ch in s:
            if ch == 'B' and stack:
                stack.pop()
            else:
                stack.append(ch)
        ans.append(str(len(stack)))
    print("\n".join(ans))

if __name__ == "__main__":
    solve()
