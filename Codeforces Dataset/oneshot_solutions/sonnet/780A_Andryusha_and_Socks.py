import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    socks = data[1:]
    
    on_table = set()
    answer = 0
    
    for sock in socks:
        if sock in on_table:
            on_table.remove(sock)
        else:
            on_table.add(sock)
            answer = max(answer, len(on_table))
    
    print(answer)

if __name__ == "__main__":
    main()
