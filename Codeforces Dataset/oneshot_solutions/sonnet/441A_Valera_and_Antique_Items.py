import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    v = int(input_data[idx + 1])
    idx += 2
    
    sellers = []
    
    for i in range(1, n + 1):
        k = int(input_data[idx])
        idx += 1
        
        can_deal = False
        for j in range(k):
            price = int(input_data[idx])
            idx += 1
            if price < v:
                can_deal = True
        
        if can_deal:
            sellers.append(i)
    
    print(len(sellers))
    if sellers:
        print(' '.join(map(str, sellers)))

if __name__ == "__main__":
    main()
