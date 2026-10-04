t = int(input())
for _ in range(t):
    n = int(input())
    num_swaps = (n + 1) // 2
    print(num_swaps)
    for i in range(1, num_swaps + 1):
        pos1 = 3 * i - 1
        pos2 = 3 * (n - i + 1)
        print(pos1, pos2)
