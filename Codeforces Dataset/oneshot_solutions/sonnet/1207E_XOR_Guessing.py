import sys

def ask(values):
    print("? " + " ".join(map(str, values)), flush=True)
    response = int(sys.stdin.readline())
    if response == -1:
        sys.exit()
    return response

def main():
    low_mask = (1 << 7) - 1
    high_mask = low_mask << 7
    
    first_query = list(range(1, 101))
    second_query = [i << 7 for i in range(1, 101)]
    
    first = ask(first_query)
    second = ask(second_query)
    
    x = (first & high_mask) | (second & low_mask)
    print("! " + str(x), flush=True)

if __name__ == "__main__":
    main()
