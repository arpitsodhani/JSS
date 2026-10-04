import sys
input = sys.stdin.readline

pattern = "FBFFBFFB"

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    # Generate enough repetitions to handle any substring
    # Need extra pattern to handle wrap-around cases
    repetitions = (n // len(pattern)) + 2
    fb_string = pattern * repetitions
    
    if s in fb_string:
        print("YES")
    else:
        print("NO")
