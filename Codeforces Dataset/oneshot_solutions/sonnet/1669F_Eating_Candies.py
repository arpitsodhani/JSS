import sys

def main():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        w = list(map(int, data[idx:idx+n]))
        idx += n
        
        alice = 0
        bob = 0
        alice_sum = 0
        bob_sum = 0
        max_candies = 0
        
        while alice + bob < n:
            if alice_sum == bob_sum:
                max_candies = alice + bob
            
            if alice_sum <= bob_sum:
                alice_sum += w[alice]
                alice += 1
            else:
                bob_sum += w[n - 1 - bob]
                bob += 1
        
        if alice_sum == bob_sum:
            max_candies = alice + bob
        
        results.append(str(max_candies))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
