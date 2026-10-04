# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def has_good_with_limit(a, b, v, l, r, limit):
    block_or = 0
    for pos in range(l, r + 1):
        if a[pos] <= limit:
            block_or |= b[pos]
            if block_or >= v:
                return True
        else:
            block_or = 0
    return False

def query_answer(a, b, v, l, r):
    values = sorted(set(a[l:r + 1]))
    lo = 0
    hi = len(values) - 1
    answer = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if has_good_with_limit(a, b, v, l, r, values[mid]):
            answer = values[mid]
            hi = mid - 1
        else:
            lo = mid + 1
    return answer

def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    k = 0
    n = data[k]
    q = data[k + 1]
    v = data[k + 2]
    k += 3
    a = [0]
    a.extend(data[k:k + n])
    k += n
    b = [0]
    b.extend(data[k:k + n])
    k += n
    result = []
    for _ in range(q):
        typ = data[k]
        k += 1
        if typ == 1:
            idx = data[k]
            val = data[k + 1]
            k += 2
            b[idx] = val
        else:
            left = data[k]
            right = data[k + 1]
            k += 2
            result.append(str(query_answer(a, b, v, left, right)))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
