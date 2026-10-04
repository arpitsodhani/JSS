# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, m = data[0], data[1]
        a = data[2:2 + n]
        b = data[2 + n:2 + n + m]

        pos = {x: i for i, x in enumerate(b)}
        c = [pos.get(x, -1) for x in a]

        ans = 0
        l = 0
        bad = 0
        arr = c + c

        for r in range(2 * n):
            if arr[r] == -1:
                l = r + 1
                bad = 0
                continue

            if r > l and arr[r - 1] != -1 and arr[r - 1] > arr[r]:
                bad += 1

            while l <= r and (r - l + 1 > n or bad > 1):
                if l < r and arr[l] > arr[l + 1]:
                    bad -= 1
                l += 1

            ans = max(ans, r - l + 1)

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
