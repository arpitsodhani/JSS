import sys
from itertools import permutations

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    nums = data[2:2 + n]

    ans = 10 ** 18

    for p in permutations(range(k)):
        mn = 10 ** 18
        mx = -1
        for s in nums:
            val = 0
            for idx in p:
                val = val * 10 + (ord(s[idx]) - 48)
            if val < mn:
                mn = val
            if val > mx:
                mx = val
        diff = mx - mn
        if diff < ans:
            ans = diff

    print(ans)

if __name__ == "__main__":
    main()
