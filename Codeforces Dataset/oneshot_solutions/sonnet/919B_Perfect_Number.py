import sys

def digit_sum(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total

def main():
    k = int(sys.stdin.readline())
    
    count = 0
    num = 18
    while True:
        num += 1
        if digit_sum(num) == 10:
            count += 1
            if count == k:
                print(num)
                return

main()
