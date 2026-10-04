import sys

def valid_part(s):
    if not (1 <= len(s) <= 16):
        return False
    for c in s:
        if not (c.isalpha() or c.isdigit() or c == '_'):
            return False
    return True

def main():
    s = sys.stdin.read().strip()
    
    if s.count('@') != 1:
        print("NO")
        return
    
    left, rest = s.split('@')
    if not valid_part(left):
        print("NO")
        return
    
    if rest.count('/') > 1:
        print("NO")
        return
    
    if '/' in rest:
        host, resource = rest.split('/')
        if not valid_part(resource):
            print("NO")
            return
    else:
        host = rest
    
    if not (1 <= len(host) <= 32):
        print("NO")
        return
    
    words = host.split('.')
    for word in words:
        if not valid_part(word):
            print("NO")
            return
    
    print("YES")

main()
