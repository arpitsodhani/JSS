# CLAUSE: setup_environment
import sys

def merge_count(arr):
    length = len(arr)
    if length < 2:
        return arr, 0
    mid = length // 2
    left, a = merge_count(arr[:mid])
    right, b = merge_count(arr[mid:])
    merged = []
    i = 0
    j = 0
    inv = a + b
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    mapping = {}
    touched = []

# CLAUSE: solve_logic
    for index in range(n):
        a = data[1 + 2 * index]
        b = data[2 + 2 * index]
        if a not in mapping:
            mapping[a] = a
            touched.append(a)
        if b not in mapping:
            mapping[b] = b
            touched.append(b)
        mapping[a], mapping[b] = mapping[b], mapping[a]

    coords = sorted(touched)
    compressed = {x: i for i, x in enumerate(coords)}
    permutation = [compressed[mapping[x]] for x in coords]
    answer = merge_count(permutation)[1]

    for x in coords:
        y = mapping[x]
        if y != x:
            answer += abs(y - x) - abs(compressed[y] - compressed[x])

# CLAUSE: finish_program
    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    main()
