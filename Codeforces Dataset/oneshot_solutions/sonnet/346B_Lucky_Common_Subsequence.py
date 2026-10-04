import sys

def compute_kmp_failure(pattern):
    m = len(pattern)
    failure = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j
    return failure

def get_next_state(k, c, virus, failure):
    while k > 0 and virus[k] != c:
        k = failure[k - 1]
    if virus[k] == c:
        return k + 1
    return 0

s1 = input().strip()
s2 = input().strip()
virus = input().strip()

n1, n2, nv = len(s1), len(s2), len(virus)

if nv == 0:
    nv = 1

failure = compute_kmp_failure(virus)

INF = -1
dp = [[[INF] * nv for _ in range(n2 + 1)] for _ in range(n1 + 1)]
parent = [[[None] * nv for _ in range(n2 + 1)] for _ in range(n1 + 1)]

dp[0][0][0] = 0

for i in range(n1 + 1):
    for j in range(n2 + 1):
        for k in range(nv):
            if dp[i][j][k] == INF:
                continue
            
            curr = dp[i][j][k]
            
            if i < n1 and dp[i+1][j][k] < curr:
                dp[i+1][j][k] = curr
                parent[i+1][j][k] = (i, j, k, None)
            
            if j < n2 and dp[i][j+1][k] < curr:
                dp[i][j+1][k] = curr
                parent[i][j+1][k] = (i, j, k, None)
            
            if i < n1 and j < n2 and s1[i] == s2[j]:
                new_k = get_next_state(k, s1[i], virus, failure) if len(virus) > 0 else 0
                if new_k < len(virus) or len(virus) == 0:
                    new_len = curr + 1
                    if dp[i+1][j+1][new_k] < new_len:
                        dp[i+1][j+1][new_k] = new_len
                        parent[i+1][j+1][new_k] = (i, j, k, s1[i])

best_len = 0
best_state = None
for k in range(nv):
    if dp[n1][n2][k] > best_len:
        best_len = dp[n1][n2][k]
        best_state = (n1, n2, k)

if best_len == 0:
    print(0)
else:
    result = []
    state = best_state
    while state and parent[state[0]][state[1]][state[2]]:
        p = parent[state[0]][state[1]][state[2]]
        if p[3]:
            result.append(p[3])
        state = (p[0], p[1], p[2])
    result.reverse()
    print(''.join(result))
