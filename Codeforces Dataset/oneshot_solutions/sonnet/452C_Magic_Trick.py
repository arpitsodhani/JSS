import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    if n == 1 and m == 1:
        print("1.0000000000000000")
        return
    
    probability = (2 * n * m - n - m) / (n * (n * m - 1))
    print("{:.16f}".format(probability))

if __name__ == "__main__":
    main()
