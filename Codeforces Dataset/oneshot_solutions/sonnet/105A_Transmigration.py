import sys

def parse_coefficient(s):
    if '.' not in s:
        return int(s), 1
    
    whole, frac = s.split('.')
    numerator = int(whole + frac)
    denominator = 10 ** len(frac)
    return numerator, denominator

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    k_str = data[idx + 2]
    idx += 3
    
    num, den = parse_coefficient(k_str)
    
    skills = {}
    for _ in range(n):
        name = data[idx]
        level = int(data[idx + 1])
        idx += 2
        
        new_level = level * num // den
        if new_level >= 100:
            skills[name] = new_level
    
    for _ in range(m):
        name = data[idx]
        idx += 1
        
        if name not in skills:
            skills[name] = 0
    
    result = sorted(skills.items())
    
    out = [str(len(result))]
    for name, level in result:
        out.append(f"{name} {level}")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
