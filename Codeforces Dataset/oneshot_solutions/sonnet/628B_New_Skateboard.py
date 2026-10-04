import sys
s = sys.stdin.readline().strip()
count = 0
for j in range(len(s)):
    # Single digit
    if int(s[j]) % 4 == 0:
        count += 1
    # Two or more digits
    if j >= 1:
        last_two = int(s[j-1:j+1])
        if last_two % 4 == 0:
            count += j
print(count)
