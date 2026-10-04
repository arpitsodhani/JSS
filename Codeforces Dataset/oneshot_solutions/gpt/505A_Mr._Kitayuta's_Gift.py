s = input().strip()

for i in range(len(s) + 1):
    for c in "abcdefghijklmnopqrstuvwxyz":
        t = s[:i] + c + s[i:]
        if t == t[::-1]:
            print(t)
            raise SystemExit

print("NA")
