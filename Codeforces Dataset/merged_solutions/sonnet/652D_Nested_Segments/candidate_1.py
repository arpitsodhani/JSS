# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def add(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx
    
    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    
    segments = []
    rights = []
    idx = 1
    for i in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        segments.append((l, r, i))
        rights.append(r)
    
    sorted_rights = sorted(rights)
    comp = {x: i + 1 for i, x in enumerate(sorted_rights)}
    
    segments.sort(key=lambda x: x[0], reverse=True)
    
    bit = Fenwick(n)
    answer = [0] * n
    
    for l, r, original_idx in segments:
        pos = comp[r]
        answer[original_idx] = bit.sum(pos - 1)
        bit.add(pos, 1)
    
    print('\n'.join(map(str, answer)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
