import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    skills = list(map(int, data[1:1 + n]))
    
    students = sorted((skills[i], i) for i in range(n))
    
    inf = 10 ** 30
    dp = [inf] * (n + 1)
    prev_size = [0] * (n + 1)
    dp[0] = 0
    
    for i in range(3, n + 1):
        for size in range(3, 6):
            if i >= size and dp[i - size] < inf:
                cost = dp[i - size] + students[i - 1][0] - students[i - size][0]
                if cost < dp[i]:
                    dp[i] = cost
                    prev_size[i] = size
    
    answer = [0] * n
    teams = 0
    pos = n
    
    while pos > 0:
        size = prev_size[pos]
        teams += 1
        for j in range(pos - size, pos):
            answer[students[j][1]] = teams
        pos -= size
    
    print(dp[n], teams)
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()
