import sys

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    result = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        
        if n % 2 == 1:
            result.append("Bob")
        elif not is_power_of_two(n):
            result.append("Alice")
        else:
            exponent = n.bit_length() - 1
            if exponent % 2 == 1:
                result.append("Bob")
            else:
                result.append("Alice")
    
    print('\n'.join(result))

main()
