# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    result = []
    for _ in range(t):
        n = data[pos]
        q = data[pos + 1]
        pos += 2
        arr = data[pos:pos + n]
        pos += n
        queries = data[pos:pos + q]
        pos += q

        freq = [0] * (n + 1)
        for value in arr:
            freq[value] += 1

        pref = [0] * (n + 1)
        total = 0
        for i in range(n + 1):
            total += freq[i]
            pref[i] = total

        need = (n + 2) // 2
        memo = {}

        for x in set(queries):
            left = 0
            right = x - 1
            while left < right:
                mid = (left + right) // 2
                count = 0
                block = 0
                while block <= n:
                    end = block + mid
                    if end > n:
                        end = n
                    if block == 0:
                        count += pref[end]
                    else:
                        count += pref[end] - pref[block - 1]
                    block += x
                if count >= need:
                    right = mid
                else:
                    left = mid + 1
            memo[x] = left

        result.append(" ".join(str(memo[x]) for x in queries))

    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
