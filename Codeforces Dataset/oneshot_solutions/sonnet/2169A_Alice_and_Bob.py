import sys

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        a = int(input_data[idx + 1])
        idx += 2
        marbles = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        left = [v for v in marbles if v < a]
        right = [v for v in marbles if v > a]
        
        if len(right) > len(left):
            # Bob chooses b > a to capture right marbles
            upper = min(2*v - a for v in right)
            b = (a + upper) // 2
        elif len(left) > len(right):
            # Bob chooses b < a to capture left marbles
            lower = max(2*v - a for v in left)
            b = (lower + a) // 2
        else:
            # Equal count or no marbles on either side
            b = 1337
        
        print(b)

if __name__ == "__main__":
    main()
