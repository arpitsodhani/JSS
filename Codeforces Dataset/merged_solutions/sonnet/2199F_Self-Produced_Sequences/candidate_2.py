# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def count_sequences(values):
    states = {0: 1}
    zero_subseq = 1
    total_sum = 0

    for x in values:
        total_sum += x
        nxt = dict(states)

        if x == 0:
            zero_subseq = (zero_subseq * 2) % MOD
            for s, c in states.items():
                nxt[s] = (nxt.get(s, 0) + c) % MOD
        else:
            same = states.get(x, 0)
            if same:
                nxt[2 * x] = (nxt.get(2 * x, 0) + same) % MOD

            target = 2 * x
            for s, c in states.items():
                if s > x and s - x == target:
                    nxt[s] = (nxt.get(s, 0) + c) % MOD

        states = nxt

    return sum(states.values()) % MOD

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    pos = 0
    t = data[pos]
    pos += 1
    ans = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n
        ans.append(str(count_sequences(arr)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
