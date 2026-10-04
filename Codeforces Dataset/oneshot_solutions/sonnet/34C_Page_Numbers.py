import sys

def main():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    pages = sorted(set(map(int, s.split(','))))
    
    result = []
    start = pages[0]
    prev = pages[0]
    
    for page in pages[1:]:
        if page == prev + 1:
            prev = page
        else:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = prev = page
    
    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")
    
    print(','.join(result))

main()
