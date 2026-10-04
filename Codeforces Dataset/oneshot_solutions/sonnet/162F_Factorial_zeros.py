n = int(input())
count = 0
power_of_5 = 5
while power_of_5 <= n:
    count += n // power_of_5
    power_of_5 *= 5
print(count)
