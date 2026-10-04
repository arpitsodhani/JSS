s = input().strip()
n = len(s)

max_time = 0
boys_count = 0
consecutive_girls = 0

for i in range(n):
    if s[i] == 'M':
        boys_count += 1
        consecutive_girls = 0
    else:  # s[i] == 'F'
        if boys_count > 0:
            time = consecutive_girls + boys_count
            max_time = max(max_time, time)
        consecutive_girls += 1

print(max_time)
