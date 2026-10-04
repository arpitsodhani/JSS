n = int(input())

answer = 0
covered = 1

while covered <= n:
    covered *= 2
    answer += 1

print(answer)
