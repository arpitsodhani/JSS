# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sushi = list(map(int, data[1:]))
    
    groups = []
    current = sushi[0]
    length = 1
    
    for i in range(1, n):
        if sushi[i] == current:
            length += 1
        else:
            groups.append(length)
            current = sushi[i]
            length = 1
    
    groups.append(length)
    
    answer = 0
    for i in range(1, len(groups)):
        answer = max(answer, 2 * min(groups[i - 1], groups[i]))
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
