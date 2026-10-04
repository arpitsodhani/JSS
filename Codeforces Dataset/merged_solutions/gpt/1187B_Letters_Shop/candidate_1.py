# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
input = sys.stdin.readline

n = int(input())
s = input().strip()

pos = [[] for _ in range(26)]
for i, ch in enumerate(s, 1):
    pos[ord(ch) - 97].append(i)

m = int(input())
ans = []

for _ in range(m):
    t = input().strip()
    cnt = [0] * 26
    best = 0
    for ch in t:
        c = ord(ch) - 97
        cnt[c] += 1
        best = max(best, pos[c][cnt[c] - 1])
    ans.append(str(best))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
