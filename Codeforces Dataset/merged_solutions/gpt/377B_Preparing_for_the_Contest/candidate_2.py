# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, s = (data[0], data[1], data[2])
    a = data[3:3 + m]
    b = data[3 + m:3 + m + n]
    c = data[3 + m + n:3 + m + n + n]
    bugs = sorted([(a[i], i) for i in range(m)], reverse=True)
    students = sorted([(b[i], c[i], i + 1) for i in range(n)], reverse=True)

    def check(days, build=False):
        heap = []
        ptr = 0
        total = 0
        ans = [0] * m if build else None
        p = 0
        while p < m:
            need = bugs[p][0]
            while ptr < n and students[ptr][0] >= need:
                heapq.heappush(heap, (students[ptr][1], students[ptr][2]))
                ptr += 1
            if not heap:
                return None if build else False
            cost, student_id = heapq.heappop(heap)
            total += cost
            if total > s:
                return None if build else False
            if build:
                for j in range(p, min(p + days, m)):
                    ans[bugs[j][1]] = student_id
            p += days
        return ans if build else True
    if not check(m):
        print('NO')
        return
    lo, hi = (1, m)
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    ans = check(lo, True)
    print('YES')
    print(*ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
