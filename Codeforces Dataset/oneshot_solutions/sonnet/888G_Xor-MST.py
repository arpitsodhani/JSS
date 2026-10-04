import sys

def first_with_bit(a, l, r, bit):
    mask = 1 << bit
    lo, hi = l, r
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] & mask:
            hi = mid
        else:
            lo = mid + 1
    return lo

def min_xor_between(a, l1, r1, l2, r2, bit):
    if l1 >= r1 or l2 >= r2:
        return 10 ** 30
    if bit < 0:
        return 0
    
    m1 = first_with_bit(a, l1, r1, bit)
    m2 = first_with_bit(a, l2, r2, bit)
    
    result = 10 ** 30
    
    if l1 < m1 and l2 < m2:
        result = min(result, min_xor_between(a, l1, m1, l2, m2, bit - 1))
    if m1 < r1 and m2 < r2:
        result = min(result, min_xor_between(a, m1, r1, m2, r2, bit - 1))
    
    if result != 10 ** 30:
        return result
    
    if l1 < m1 and m2 < r2:
        result = min(result, min_xor_between(a, l1, m1, m2, r2, bit - 1))
    if m1 < r1 and l2 < m2:
        result = min(result, min_xor_between(a, m1, r1, l2, m2, bit - 1))
    
    return result + (1 << bit)

def mst_cost(a, l, r, bit):
    if r - l <= 1 or bit < 0:
        return 0
    
    mid = first_with_bit(a, l, r, bit)
    
    result = mst_cost(a, l, mid, bit - 1) + mst_cost(a, mid, r, bit - 1)
    
    if l < mid and mid < r:
        result += (1 << bit) + min_xor_between(a, l, mid, mid, r, bit - 1)
    
    return result

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    a.sort()
    
    if n <= 1:
        print(0)
        return
    
    max_bit = max(a).bit_length() - 1
    print(mst_cost(a, 0, n, max_bit))

if __name__ == "__main__":
    main()
