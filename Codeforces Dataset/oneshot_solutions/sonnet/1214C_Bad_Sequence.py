import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    
    balance = 0
    min_balance = 0
    
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance == 0 and min_balance >= -1:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
