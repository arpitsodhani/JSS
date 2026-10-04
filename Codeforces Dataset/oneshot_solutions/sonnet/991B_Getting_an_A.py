import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    grades = list(map(int, input_data[1:n+1]))
    
    current_sum = sum(grades)
    target = 4.5 * n
    
    if current_sum >= target:
        print(0)
        return
    
    grades.sort()
    
    new_sum = current_sum
    for k in range(1, n + 1):
        new_sum = new_sum - grades[k-1] + 5
        
        if new_sum >= target:
            print(k)
            return

solve()
