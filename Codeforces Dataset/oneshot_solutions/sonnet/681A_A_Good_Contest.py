n = int(input())
good = False
for _ in range(n):
    parts = input().split()
    before = int(parts[1])
    after = int(parts[2])
    if before >= 2400 and after > before:
        good = True

print("YES" if good else "NO")
