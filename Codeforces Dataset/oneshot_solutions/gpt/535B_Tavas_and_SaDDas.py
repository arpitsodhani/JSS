n = input().strip()

ans = (1 << len(n)) - 1
for c in n:
    ans = ans * 2 + (1 if c == '7' else 0)

print(ans)
