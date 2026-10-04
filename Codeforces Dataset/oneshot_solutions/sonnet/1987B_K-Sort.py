import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        current_max = 0
        total_needed = 0
        max_needed = 0
        
        for i in range(n):
            x = data[idx]
            idx += 1
            
            if i == 0:
                current_max = x
            elif x < current_max:
                need = current_max - x
                total_needed += need
                if need > max_needed:
                    max_needed = need
            else:
                current_max = x
        
        answers.append(str(total_needed + max_needed))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
