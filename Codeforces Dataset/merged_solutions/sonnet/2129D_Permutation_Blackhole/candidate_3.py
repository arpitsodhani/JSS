# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def put(mp, key, value):
    mp[key] = (mp.get(key, 0) + value) % MOD

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    q = nums[0]
    p = 1
    cases = []
    lim = 0
    for _ in range(q):
        n = nums[p]
        p += 1
        arr = nums[p:p + n]
        p += n
        cases.append((n, arr))
        lim = max(lim, n)

    c = [[0] * (lim + 1) for _ in range(lim + 1)]
    for i in range(lim + 1):
        row = c[i]
        row[0] = 1
        row[i] = 1
        prev = c[i - 1] if i else row
        for j in range(1, i):
            row[j] = (prev[j - 1] + prev[j]) % MOD

    answers = []
    for n, fixed in cases:
        b = n + 1
        valid = [[False] * (n + 1) for _ in range(n + 1)]
        for pos in range(1, n + 1):
            need = fixed[pos - 1]
            if need == -1:
                for val in range(n + 1):
                    valid[pos][val] = True
            elif 0 <= need <= n:
                valid[pos][need] = True

        both = [[{} for _ in range(n + 2)] for __ in range(n + 2)]
        right = [[{} for _ in range(n + 2)] for __ in range(n + 2)]
        left = [[{} for _ in range(n + 2)] for __ in range(n + 2)]

        for i in range(1, n + 1):
            right[i][i] = {0: 1}
            left[i][i] = {0: 1}
        for i in range(1, n):
            both[i][i + 1] = {0: 1}

        for d in range(1, n + 1):
            for l in range(1, n - d + 1):
                r = l + d
                target = right[l][r]
                for x in range(l + 1, r + 1):
                    ways = c[d - 1][x - l - 1]
                    left_map = both[l][x]
                    right_map = right[x][r]
                    for packed, cnt1 in left_map.items():
                        edge_l = packed // b
                        score_x_l = packed - edge_l * b
                        for score_x_r, cnt2 in right_map.items():
                            if valid[x][score_x_l + score_x_r]:
                                put(target, edge_l + 1, cnt1 * cnt2 * ways)

            for r in range(2, n + d + 1):
                l = r - d
                if l < 1 or l > n:
                    continue
                target = left[l][r]
                for x in range(l, r):
                    ways = c[d - 1][x - l]
                    left_map = left[l][x]
                    right_map = both[x][r]
                    for score_x_l, cnt1 in left_map.items():
                        for packed, cnt2 in right_map.items():
                            score_x_r = packed // b
                            edge_r = packed - score_x_r * b
                            if valid[x][score_x_l + score_x_r]:
                                put(target, edge_r + 1, cnt1 * cnt2 * ways)

            width = d + 1
            for l in range(1, n - width + 2):
                r = l + width
                target = both[l][r]
                for x in range(l + 1, r):
                    left_part = x - l - 1
                    right_part = r - x - 1
                    ways = c[left_part + right_part][left_part]
                    inc_l = int(x - l <= r - x)
                    inc_r = 1 - inc_l
                    for packed_l, cnt1 in both[l][x].items():
                        edge_l = packed_l // b
                        score_x_l = packed_l - edge_l * b
                        for packed_r, cnt2 in both[x][r].items():
                            score_x_r = packed_r // b
                            edge_r = packed_r - score_x_r * b
                            if valid[x][score_x_l + score_x_r]:
                                put(target, (edge_l + inc_l) * b + edge_r + inc_r, cnt1 * cnt2 * ways)

        total = 0
        for root in range(1, n + 1):
            ways = c[n - 1][root - 1]
            for ls, cnt1 in left[1][root].items():
                for rs, cnt2 in right[root][n].items():
                    if valid[root][ls + rs]:
                        total = (total + cnt1 * cnt2 * ways) % MOD
        answers.append(str(total))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
