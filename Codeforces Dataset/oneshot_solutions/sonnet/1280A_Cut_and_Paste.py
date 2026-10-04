import sys

MOD = 10 ** 9 + 7

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        x = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        chars = list(s)
        length = len(chars)
        
        for i in range(x):
            repeat = ord(chars[i]) - ord('0')
            suffix_len = length - i - 1
            length = (i + 1 + suffix_len * repeat) % MOD
            
            if len(chars) < x:
                suffix = chars[i + 1:]
                need = x - len(chars)
                add = suffix * (repeat - 1)
                if len(add) > need:
                    add = add[:need]
                chars.extend(add)
        
        answers.append(str(length))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
