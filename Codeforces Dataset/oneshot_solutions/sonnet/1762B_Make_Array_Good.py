import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        results.append(str(n))
        for i in range(n):
            # Find smallest power of 2 >= a[i]
            power = 1
            while power < a[i]:
                power *= 2
            
            # Add (power - a[i]) to a[i]
            x = power - a[i]
            results.append(f"{i+1} {x}")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
