import sys

def main():
    data = sys.stdin.read().split()
    
    if len(data) >= 2:
        s = data[1]
    else:
        token = data[0]
        i = 0
        while i < len(token) and token[i].isdigit():
            i += 1
        s = token
        for cut in range(1, len(token) + 1):
            if cut + int(token[:cut]) == len(token):
                s = token[cut:]
                break
    
    parts = s.split('0')
    result = ''.join(str(len(part)) for part in parts)
    print(result)

if __name__ == "__main__":
    main()
