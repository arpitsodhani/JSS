import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split()
    if len(data) == 1:
        raw = data[0]
        n = int(raw[0])
        boards = []
        pos = 1
        for _ in range(4):
            board = raw[pos:pos + n * n]
            pos += n * n
            boards.append(board)
    else:
        n = int(data[0])
        boards = []
        idx = 1
        for _ in range(4):
            board = ''.join(data[idx:idx + n])
            idx += n
            boards.append(board)
    
    cost = [[0, 0] for _ in range(4)]
    
    for b in range(4):
        for i in range(n):
            for j in range(n):
                val = int(boards[b][i * n + j])
                expected = (i + j) & 1
                if val != expected:
                    cost[b][0] += 1
                else:
                    cost[b][1] += 1
    
    answer = 10 ** 18
    indices = range(4)
    
    for first in combinations(indices, 2):
        first = set(first)
        cur = 0
        for i in indices:
            if i in first:
                cur += cost[i][0]
            else:
                cur += cost[i][1]
        answer = min(answer, cur)
    
    print(answer)

if __name__ == "__main__":
    main()
