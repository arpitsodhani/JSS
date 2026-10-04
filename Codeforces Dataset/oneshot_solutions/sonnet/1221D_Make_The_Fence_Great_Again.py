import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    
    answers = []
    inf = 10 ** 30
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        
        a = [0] * n
        b = [0] * n
        for i in range(n):
            a[i] = int(data[idx])
            b[i] = int(data[idx + 1])
            idx += 2
        
        dp = [0, b[0], 2 * b[0]]
        
        for i in range(1, n):
            new_dp = [inf, inf, inf]
            for add in range(3):
                height = a[i] + add
                cost = add * b[i]
                for prev_add in range(3):
                    if a[i - 1] + prev_add != height:
                        new_dp[add] = min(new_dp[add], dp[prev_add] + cost)
            dp = new_dp
        
        answers.append(str(min(dp)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
