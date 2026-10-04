# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import heapq

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, m = data[0], data[1]
        start_to_end = {}
        end_to_start = {}
        heap = []
        car_pos = {}

        def best(l, r):
            if l == 1 and r == n:
                return n + 1, 1
            if l == 1:
                return r, 1
            if r == n:
                return n - l + 1, n
            x = (l + r) // 2
            return x - l + 1, x

        def add_interval(l, r):
            if l > r:
                return
            start_to_end[l] = r
            end_to_start[r] = l
            score, pos = best(l, r)
            heapq.heappush(heap, (-score, pos, l, r))

        def remove_interval(l, r):
            del start_to_end[l]
            del end_to_start[r]

        add_interval(1, n)
        ans = []
        idx = 2

        for _ in range(m):
            t = data[idx]
            cid = data[idx + 1]
            idx += 2

            if t == 1:
                while True:
                    _, pos, l, r = heapq.heappop(heap)
                    if start_to_end.get(l) == r:
                        break

                remove_interval(l, r)
                car_pos[cid] = pos
                ans.append(str(pos))

                add_interval(l, pos - 1)
                add_interval(pos + 1, r)
            else:
                pos = car_pos.pop(cid)
                l = r = pos

                left_l = end_to_start.get(pos - 1)
                if left_l is not None:
                    remove_interval(left_l, pos - 1)
                    l = left_l

                right_r = start_to_end.get(pos + 1)
                if right_r is not None:
                    remove_interval(pos + 1, right_r)
                    r = right_r

                add_interval(l, r)

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
