s = input().strip()
i = 0
while i < len(s):
    if s[i:i+3] == "144":
        i += 3
    elif s[i:i+2] == "14":
        i += 2
    elif s[i] == "1":
        i += 1
    else:
        print("NO")
        exit()
print("YES")
