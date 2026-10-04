x = input().strip()
y = input().strip()

possible = True
for i in range(len(x)):
    if y[i] > x[i]:
        possible = False
        break

if possible:
    print(y)
else:
    print(-1)
