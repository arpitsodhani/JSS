import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    s = data[idx + 2]
    idx += 3
    
    bugs = []
    for i in range(m):
        bugs.append((data[idx], i))
        idx += 1
    
    abilities = data[idx:idx + n]
    idx += n
    costs = data[idx:idx + n]
    
    bugs.sort(reverse=True)
    students = sorted([(abilities[i], costs[i], i + 1) for i in range(n)], reverse=True)
    
    def check(days, build=False):
        heap = []
        ptr = 0
        total_cost = 0
        answer = [0] * m if build else None
        
        for start in range(0, m, days):
            needed = bugs[start][0]
            
            while ptr < n and students[ptr][0] >= needed:
                ability, cost, student_id = students[ptr]
                heapq.heappush(heap, (cost, student_id))
                ptr += 1
            
            if not heap:
                return None if build else False
            
            cost, student_id = heapq.heappop(heap)
            total_cost += cost
            
            if total_cost > s:
                return None if build else False
            
            if build:
                for j in range(start, min(start + days, m)):
                    answer[bugs[j][1]] = student_id
        
        return answer if build else True
    
    if not check(m):
        print("NO")
        return
    
    left, right = 1, m
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    answer = check(left, True)
    print("YES")
    print(" ".join(map(str, answer)))

if __name__ == "__main__":
    main()
