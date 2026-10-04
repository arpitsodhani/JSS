# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from array import array

    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    virus = sys.stdin.readline().strip()

    n, m, L = len(s1), len(s2), len(virus)

    pi = [0] * L
    for i in range(1, L):
        j = pi[i - 1]
        while j > 0 and virus[i] != virus[j]:
            j = pi[j - 1]
        if virus[i] == virus[j]:
            j += 1
        pi[i] = j

    go = [[0] * 26 for _ in range(L)]
    for k in range(L):
        for c in range(26):
            ch = chr(65 + c)
            j = k
            while j > 0 and ch != virus[j]:
                j = pi[j - 1]
            if ch == virus[j]:
                j += 1
            go[k][c] = j

    W = (m + 1) * L
    size = (n + 1) * (m + 1) * L
    dp = array('h', [0]) * size
    par = bytearray(size)

    for i in range(n - 1, -1, -1):
        base_i = i * W
        base_ip = (i + 1) * W
        for j in range(m - 1, -1, -1):
            base = base_i + j * L
            down = base_ip + j * L
            right = base_i + (j + 1) * L
            diag = base_ip + (j + 1) * L
            for k in range(L):
                best = dp[down + k]
                act = 1
                if dp[right + k] > best:
                    best = dp[right + k]
                    act = 2
                if s1[i] == s2[j]:
                    nk = go[k][ord(s1[i]) - 65]
                    if nk < L and dp[diag + nk] + 1 > best:
                        best = dp[diag + nk] + 1
                        act = 3
                dp[base + k] = best
                par[base + k] = act

    if dp[0] == 0:
        print(0)
    else:
        ans = []
        i = j = k = 0
        while i < n and j < m:
            idx = i * W + j * L + k
            act = par[idx]
            if act == 1:
                i += 1
            elif act == 2:
                j += 1
            elif act == 3:
                ans.append(s1[i])
                k = go[k][ord(s1[i]) - 65]
                i += 1
                j += 1
            else:
                break
        print(''.join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
