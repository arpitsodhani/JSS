import sys

def solve(a):
    n = len(a)
    
    # Precompute elements from position i to n-1
    suffix_elements = [set() for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        suffix_elements[i] = suffix_elements[i + 1] | {a[i]}
    
    required = set()
    current_elements = set()
    count = 0
    
    for i in range(n):
        current_elements.add(a[i])
        
        # Check if we can cut at position i+1
        if i < n - 1:
            # Check if current segment contains all required elements
            if required.issubset(current_elements):
                # Check if all current elements appear in the remaining part
                if current_elements.issubset(suffix_elements[i + 1]):
                    # Make a cut
                    count += 1
                    required = current_elements.copy()
                    current_elements = set()
    
    # Last segment
    count += 1
    
    return count

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        print(solve(a))

if __name__ == "__main__":
    main()
