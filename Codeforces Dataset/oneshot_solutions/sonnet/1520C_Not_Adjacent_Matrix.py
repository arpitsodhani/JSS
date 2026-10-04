import sys

def solve(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return None
    
    # Generate odd numbers then even numbers
    odds = list(range(1, n*n + 1, 2))
    evens = list(range(2, n*n + 1, 2))
    nums = odds + evens
    
    # Fill matrix row by row
    matrix = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(nums[idx])
            idx += 1
        matrix.append(row)
    
    return matrix

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        result = solve(n)
        
        if result is None:
            print(-1)
        else:
            for row in result:
                print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
