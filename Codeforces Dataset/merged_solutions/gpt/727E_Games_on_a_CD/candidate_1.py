# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    s = data[2]
    g = int(data[3])
    games = data[4:4 + g]

    total = n * k
    ss = s + s[:k - 1]

    mod1 = 1000000007
    mod2 = 1000000009
    base = 911382323

    max_len = len(ss)
    pow1 = [1] * (max_len + 1)
    pow2 = [1] * (max_len + 1)
    for i in range(max_len):
        pow1[i + 1] = (pow1[i] * base) % mod1
        pow2[i + 1] = (pow2[i] * base) % mod2

    pref1 = [0] * (max_len + 1)
    pref2 = [0] * (max_len + 1)
    for i, ch in enumerate(ss):
        pref1[i + 1] = (pref1[i] * base + ch) % mod1
        pref2[i + 1] = (pref2[i] * base + ch) % mod2

    def sub_hash(l, r):
        h1 = (pref1[r] - pref1[l] * pow1[r - l]) % mod1
        h2 = (pref2[r] - pref2[l] * pow2[r - l]) % mod2
        return h1, h2

    mp = {}
    for idx, word in enumerate(games, 1):
        h1 = 0
        h2 = 0
        for ch in word:
            h1 = (h1 * base + ch) % mod1
            h2 = (h2 * base + ch) % mod2
        mp[(h1, h2)] = idx

    ids = [0] * total
    for i in range(total):
        ids[i] = mp.get(sub_hash(i, i + k), 0)

    seen = [0] * (g + 1)
    mark = 0

    for start in range(k):
        mark += 1
        ans = []
        ok = True

        pos = start
        for _ in range(n):
            game_id = ids[pos]
            if game_id == 0 or seen[game_id] == mark:
                ok = False
                break
            seen[game_id] = mark
            ans.append(game_id)
            pos += k
            if pos >= total:
                pos -= total

        if ok:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, ans)))
            return

    sys.stdout.write("NO")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
