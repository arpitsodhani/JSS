# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    q = data[idx + 1]
    idx += 2
    
    colors = data[idx:idx + n]
    idx += n
    
    first_pos = {}
    for i, color in enumerate(colors, 1):
        if color not in first_pos:
            first_pos[color] = i
    
    result = []
    for color in data[idx:idx + q]:
        pos = first_pos[color]
        result.append(str(pos))
        
        for other in first_pos:
            if first_pos[other] < pos:
                first_pos[other] += 1
        first_pos[color] = 1
    
    print(' '.join(result))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
