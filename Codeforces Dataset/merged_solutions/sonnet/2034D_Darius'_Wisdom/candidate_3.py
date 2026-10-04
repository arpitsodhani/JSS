# CLAUSE: setup_environment
import sys

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    p = 1
    res = []

# CLAUSE: solve_logic
    for _ in range(nums[0]):
        n = nums[p]
        p += 1
        arr = nums[p:p + n]
        p += n

        need_zero = 0
        need_one = 0
        for x in arr:
            if x == 0:
                need_zero += 1
            elif x == 1:
                need_one += 1

        after_zero = []
        one_places = []
        for i, x in enumerate(arr):
            if x == 1:
                one_places.append(i)
            if x == 0 and i >= need_zero:
                after_zero.append(i)

        moves = []

        def refresh_take_one():
            while one_places and arr[one_places[-1]] != 1:
                one_places.pop()
            return one_places[-1]

        def refresh_take_zero():
            while after_zero and (arr[after_zero[-1]] != 0 or after_zero[-1] < need_zero):
                after_zero.pop()
            return after_zero.pop()

        def exchange(i, j):
            if arr[i] > arr[j]:
                moves.append((i + 1, j + 1))
            else:
                moves.append((j + 1, i + 1))
            arr[i], arr[j] = arr[j], arr[i]
            if arr[i] == 1:
                one_places.append(i)
            if arr[j] == 1:
                one_places.append(j)
            if i >= need_zero and arr[i] == 0:
                after_zero.append(i)
            if j >= need_zero and arr[j] == 0:
                after_zero.append(j)

        for i in range(need_zero):
            if arr[i] == 0:
                continue
            j = refresh_take_zero()
            if arr[i] == 2:
                k = refresh_take_one()
                exchange(i, k)
            exchange(i, j)

        end_one = need_zero + need_one
        right_ones = [i for i in range(end_one, n) if arr[i] == 1]
        for i in range(need_zero, end_one):
            if arr[i] == 2:
                exchange(i, right_ones.pop())

        res.append(str(len(moves)))
        res.extend(str(u) + " " + str(v) for u, v in moves)

# CLAUSE: finish_program
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
