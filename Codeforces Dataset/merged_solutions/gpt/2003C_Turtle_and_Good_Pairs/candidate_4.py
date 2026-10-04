# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import heapq

    def build(s):
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1

        heap = [(-v, ch) for ch, v in cnt.items()]
        heapq.heapify(heap)

        res = []
        while heap:
            c1, ch1 = heapq.heappop(heap)

            if res and ch1 == res[-1] and heap:
                c2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                c2 += 1
                if c2 < 0:
                    heapq.heappush(heap, (c2, ch2))
                heapq.heappush(heap, (c1, ch1))
            else:
                res.append(ch1)
                c1 += 1
                if c1 < 0:
                    heapq.heappush(heap, (c1, ch1))

        return ''.join(res)

    def main():
        data = sys.stdin.read().split()
        if not data:
            return

        t = int(data[0])
        ans = []
        p = 1

        for _ in range(t):
            n = int(data[p])
            s = data[p + 1]
            p += 2
            ans.append(build(s))

        sys.stdout.write('\n'.join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
