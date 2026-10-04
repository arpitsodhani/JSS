import sys
from bisect import bisect_right

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def add(self, idx, val):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx
    
    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    q = int(data[0])
    idx = 1
    
    queries = []
    times_by_value = {}
    
    for _ in range(q):
        op = int(data[idx])
        time = int(data[idx + 1])
        value = int(data[idx + 2])
        idx += 3
        
        queries.append((op, time, value))
        
        if op != 3:
            if value not in times_by_value:
                times_by_value[value] = []
            times_by_value[value].append(time)
    
    coords = {}
    trees = {}
    for value, times in times_by_value.items():
        sorted_times = sorted(set(times))
        coords[value] = sorted_times
        trees[value] = Fenwick(len(sorted_times))
    
    answer = []
    
    for op, time, value in queries:
        if op == 3:
            if value not in coords:
                answer.append("0")
            else:
                pos = bisect_right(coords[value], time)
                answer.append(str(trees[value].sum(pos)))
        else:
            delta = 1 if op == 1 else -1
            pos = bisect_right(coords[value], time)
            trees[value].add(pos, delta)
    
    sys.stdout.write("\n".join(answer))

if __name__ == "__main__":
    main()
