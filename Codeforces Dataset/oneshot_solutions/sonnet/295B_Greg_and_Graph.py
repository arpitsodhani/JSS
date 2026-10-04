import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    dist = []
    for _ in range(n):
        dist.append(data[idx:idx + n])
        idx += n
    
    order = [x - 1 for x in data[idx:idx + n]]
    
    active = [False] * n
    answers = []
    
    for k in reversed(order):
        active[k] = True
        
        for i in range(n):
            dik = dist[i][k]
            for j in range(n):
                nd = dik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
        
        total = 0
        for i in range(n):
            if active[i]:
                row = dist[i]
                for j in range(n):
                    if active[j]:
                        total += row[j]
        
        answers.append(total)
    
    answers.reverse()
    print(' '.join(map(str, answers)))

if __name__ == "__main__":
    main()
