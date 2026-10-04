# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def tri(n):
    return n * (n + 1) // 2

def tail_sum(days, length):
    if length <= 0:
        return 0
    return tri(days) - tri(days - length)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    months = data[2:]
    
    months *= 2
    
    left = 0
    days_sum = 0
    hugs_sum = 0
    answer = 0
    
    for right in range(2 * n):
        days_sum += months[right]
        hugs_sum += tri(months[right])
        
        while days_sum > x:
            days_sum -= months[left]
            hugs_sum -= tri(months[left])
            left += 1
        
        need = x - days_sum
        current = hugs_sum
        
        if need > 0 and left > 0:
            current += tail_sum(months[left - 1], need)
        
        if days_sum == x or left > 0:
            answer = max(answer, current)
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
