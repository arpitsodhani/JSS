# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    k = int(sys.stdin.readline())
    
    bits = []
    x = k
    pos = 0
    while x:
        if x & 1:
            bits.append(pos)
        x >>= 1
        pos += 1
    
    if k == 1:
        print(2)
        print("NY")
        print("YN")
        return
    
    max_bit = max(bits)
    n = 2 + 2 * max_bit
    graph = [['N'] * n for _ in range(n)]
    
    def add(u, v):
        graph[u][v] = 'Y'
        graph[v][u] = 'Y'
    
    source = 0
    target = 1
    
    levels = []
    for i in range(max_bit + 1):
        if i == 0:
            levels.append([source])
        else:
            levels.append([2 + 2 * (i - 1), 3 + 2 * (i - 1)])
    
    for i in range(max_bit):
        for u in levels[i]:
            for v in levels[i + 1]:
                add(u, v)
    
    if 0 in bits:
        add(source, target)
    
    for b in bits:
        if b > 0:
            add(levels[b][0], target)
    
    print(n)
    for row in graph:
        print(''.join(row))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
