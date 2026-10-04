import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]

    ans = 0
    stack = []

    for x in a:
        while stack and stack[-1] < x:
            ans = max(ans, stack[-1] ^ x)
            stack.pop()
        if stack:
            ans = max(ans, stack[-1] ^ x)
        stack.append(x)

    print(ans)

if __name__ == "__main__":
    main()
