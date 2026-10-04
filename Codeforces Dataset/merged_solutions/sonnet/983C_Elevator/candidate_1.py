# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from heapq import heappush, heappop

def generate_codes(pos, remaining, code, powers, codes):
    if pos == 10:
        codes.append(code)
        return
    for count in range(remaining + 1):
        generate_codes(pos + 1, remaining - count, code + count * powers[pos], powers, codes)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    
    starts = []
    ends = []
    idx = 1
    for _ in range(n):
        starts.append(data[idx])
        ends.append(data[idx + 1])
        idx += 2
    
    powers = [0] * 10
    powers[1] = 1
    for i in range(2, 10):
        powers[i] = powers[i - 1] * 5
    base = powers[9] * 5
    
    codes = []
    generate_codes(1, 4, 0, powers, codes)
    
    total = {}
    present = {}
    drop_count = {}
    drop_code = {}
    
    for code in codes:
        cur_total = 0
        cur_present = []
        cur_drop_count = [0] * 10
        cur_drop_code = [0] * 10
        
        for floor in range(1, 10):
            count = (code // powers[floor]) % 5
            cur_total += count
            cur_drop_count[floor] = count
            cur_drop_code[floor] = code - count * powers[floor]
            if count:
                cur_present.append(floor)
        
        total[code] = cur_total
        present[code] = cur_present
        drop_count[code] = cur_drop_count
        drop_code[code] = cur_drop_code
    
    def make_key(next_person, floor, code):
        return ((next_person * 9 + (floor - 1)) * base + code)
    
    start_key = make_key(0, 1, 0)
    dist = {start_key: 0}
    heap = [(0, start_key)]
    
    while heap:
        cur_dist, key = heappop(heap)
        if dist.get(key) != cur_dist:
            continue
        
        code = key % base
        temp = key // base
        floor = temp % 9 + 1
        next_person = temp // 9
        
        if next_person == n and code == 0:
            print(cur_dist)
            return
        
        candidates = present[code]
        next_start = starts[next_person] if next_person < n else 0
        
        for target in candidates:
            removed = drop_count[code][target]
            new_code = drop_code[code][target]
            load = total[new_code]
            j = next_person
            added = 0
            
            while j < n and load < 4 and starts[j] == target:
                new_code += powers[ends[j]]
                load += 1
                added += 1
                j += 1
            
            cost = abs(floor - target) + removed + added
            new_key = make_key(j, target, new_code)
            new_dist = cur_dist + cost
            
            if new_dist < dist.get(new_key, 10 ** 18):
                dist[new_key] = new_dist
                heappush(heap, (new_dist, new_key))
        
        if next_start and drop_count[code][next_start] == 0:
            target = next_start
            if total[code] < 4:
                new_code = code
                load = total[code]
                j = next_person
                added = 0
                
                while j < n and load < 4 and starts[j] == target:
                    new_code += powers[ends[j]]
                    load += 1
                    added += 1
                    j += 1
                
                cost = abs(floor - target) + added
                new_key = make_key(j, target, new_code)
                new_dist = cur_dist + cost
                
                if new_dist < dist.get(new_key, 10 ** 18):
                    dist[new_key] = new_dist
                    heappush(heap, (new_dist, new_key))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
