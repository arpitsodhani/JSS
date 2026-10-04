# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    a = data[2:2 + n]
    
    powers = []
    limit = 10 ** 15
    
    if k == 1:
        powers = [1]
    elif k == -1:
        powers = [1, -1]
    elif k == 0:
        powers = [1, 0]
    else:
        value = 1
        while abs(value) <= limit:
            powers.append(value)
            value *= k
    
    count = defaultdict(int)
    count[0] = 1
    
    prefix = 0
    answer = 0
    
    for x in a:
        prefix += x
        for p in powers:
            answer += count[prefix - p]
        count[prefix] += 1
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
