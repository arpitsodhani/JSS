import sys

def is_palindrome(s):
    return s == s[::-1]

def main():
    s = sys.stdin.readline().strip()
    
    for i in range(len(s) + 1):
        for c in "abcdefghijklmnopqrstuvwxyz":
            candidate = s[:i] + c + s[i:]
            if is_palindrome(candidate):
                print(candidate)
                return
    
    print("NA")

if __name__ == "__main__":
    main()
