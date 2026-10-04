import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    bars = data[1:1 + n]
    
    left = 0
    right = n - 1
    alice_time = 0
    bob_time = 0
    alice = 0
    bob = 0
    
    while left <= right:
        if alice_time <= bob_time:
            alice_time += bars[left]
            alice += 1
            left += 1
        else:
            bob_time += bars[right]
            bob += 1
            right -= 1
    
    print(alice, bob)

if __name__ == "__main__":
    main()
