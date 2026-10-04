# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    p = [0] + data[1:1 + n]
    
    visited = [False] * (n + 1)
    lengths = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            cur = i
            length = 0
            while not visited[cur]:
                visited[cur] = True
                length += 1
                cur = p[cur]
            lengths.append(length)
    
    lengths.sort(reverse=True)
    
    if len(lengths) >= 2:
        lengths[0] += lengths[1]
        lengths.pop(1)
    
    answer = sum(x * x for x in lengths)
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
