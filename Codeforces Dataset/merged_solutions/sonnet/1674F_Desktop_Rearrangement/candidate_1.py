# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    q = int(data[idx + 2])
    idx += 3
    
    grid = []
    size = n * m
    bit = [0] * (size + 1)
    total = 0
    
    def add(pos, val):
        while pos <= size:
            bit[pos] += val
            pos += pos & -pos
    
    def query(pos):
        s = 0
        while pos > 0:
            s += bit[pos]
            pos -= pos & -pos
        return s
    
    for i in range(n):
        row = data[idx].decode()
        idx += 1
        grid.append(list(row))
        for j, ch in enumerate(row):
            if ch == '*':
                pos = j * n + i + 1
                add(pos, 1)
                total += 1
    
    out = []
    for _ in range(q):
        x = int(data[idx]) - 1
        y = int(data[idx + 1]) - 1
        idx += 2
        
        pos = y * n + x + 1
        
        if grid[x][y] == '*':
            grid[x][y] = '.'
            add(pos, -1)
            total -= 1
        else:
            grid[x][y] = '*'
            add(pos, 1)
            total += 1
        
        icons_in_prefix = query(total)
        out.append(str(total - icons_in_prefix))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
