import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        s = data[idx]
        p = int(data[idx + 1])
        idx += 2
        
        total = sum(ord(c) - 96 for c in s)
        remove_count = [0] * 26
        
        for value in range(26, 0, -1):
            if total <= p:
                break
            
            cnt = s.count(chr(value + 96))
            need = total - p
            take = min(cnt, (need + value - 1) // value)
            remove_count[value - 1] = take
            total -= take * value
        
        result = []
        for c in s:
            pos = ord(c) - 97
            if remove_count[pos] > 0:
                remove_count[pos] -= 1
            else:
                result.append(c)
        
        answers.append(''.join(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
