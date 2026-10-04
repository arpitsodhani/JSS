# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(stream)
    output = []

    for _ in range(t):
        n = next(stream)
        k = next(stream)
        colors = [next(stream) for _ in range(n)]

        compressed = {}
        for x in colors:
            if x not in compressed:
                compressed[x] = len(compressed)

        occ = [[] for _ in range(len(compressed))]
        dp_len = [0] * (n + 1)
        dp_count = [0] * (n + 1)
        dp_count[0] = 1

        i = 1
        while i <= n:
            dp_len[i] = dp_len[i - 1]
            dp_count[i] = dp_count[i - 1]

            color_id = compressed[colors[i - 1]]
            occ[color_id].append(i)

            if len(occ[color_id]) >= k:
                start_index = occ[color_id][-k] - 1
                new_len = dp_len[start_index] + 1
                if new_len == dp_len[i]:
                    dp_count[i] = (dp_count[i] + dp_count[start_index]) % MOD
                elif new_len > dp_len[i]:
                    dp_len[i] = new_len
                    dp_count[i] = dp_count[start_index]

            i += 1

        output.append(str(dp_count[n] % MOD))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
