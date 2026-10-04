import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    
    remove = [0] * 26
    
    for c in s:
        remove[ord(c) - ord('a')] += 1
    
    left = k
    for i in range(26):
        take = min(left, remove[i])
        remove[i] = take
        left -= take
        if left == 0:
            break
    
    result = []
    for c in s:
        idx = ord(c) - ord('a')
        if remove[idx] > 0:
            remove[idx] -= 1
        else:
            result.append(c)
    
    print(''.join(result))

if __name__ == "__main__":
    main()
