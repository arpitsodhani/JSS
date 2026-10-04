import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    q = data[idx + 1]
    idx += 2
    
    values = data[idx:idx + n]
    idx += n
    
    colors = data[idx:idx + n]
    idx += n
    
    max_color = max(colors) if colors else 0
    dp = [0] * (max_color + 1)
    seen = [0] * (max_color + 1)
    timer = 0
    
    answers = []
    
    for _ in range(q):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        
        timer += 1
        best1_value = 0
        best1_color = -1
        best2_value = 0
        
        for value, color in zip(values, colors):
            if seen[color] != timer:
                seen[color] = timer
                dp[color] = 0
            
            current = dp[color]
            
            same_color = current + value * a
            if color == best1_color:
                different_color = best2_value + value * b
            else:
                different_color = best1_value + value * b
            
            new_value = max(current, same_color, different_color)
            
            if new_value != current:
                dp[color] = new_value
                
                if color == best1_color:
                    best1_value = new_value
                elif new_value > best1_value:
                    best2_value = best1_value
                    best1_value = new_value
                    best1_color = color
                elif new_value > best2_value:
                    best2_value = new_value
        
        answers.append(str(best1_value))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
