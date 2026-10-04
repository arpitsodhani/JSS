import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    
    max_sum = n * (n - 1) // 2
    if k > max_sum:
        print("Impossible")
        return
    
    depths = [0] * n
    remaining = k
    
    for i in range(n - 1, 0, -1):
        take = min(i, remaining)
        depths[i] = take
        remaining -= take
    
    result = []
    balance = 0
    
    for depth in depths:
        while balance > depth:
            result.append(')')
            balance -= 1
        result.append('(')
        balance += 1
    
    result.append(')' * balance)
    print(''.join(result))

if __name__ == "__main__":
    main()
