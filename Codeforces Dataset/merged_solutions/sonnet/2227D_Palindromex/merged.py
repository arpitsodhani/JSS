import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + 2 * n])
        pos += 2 * n
    return cases

# Clause palindrome_radii [Confidence: 1.00]
def palindrome_radii(a):
    spaced = [-1]
    for element in a:
        spaced.append(element)
        spaced.append(-1)
    size = len(spaced)
    radius = [0] * size
    centre = 0
    edge = 0
    for i in range(size):
        if i < edge:
            mirror = radius[2 * centre - i]
            room = edge - i
            radius[i] = mirror if mirror < room else room
        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < size and \
                spaced[i - radius[i] - 1] == spaced[i + radius[i] + 1]:
            radius[i] += 1
        if i + radius[i] > edge:
            centre = i
            edge = i + radius[i]
    return radius

# Clause centre_values [Confidence: 1.00]
def centre_values(a, radius):
    seen = {}
    for i in range(len(a)):
        if a[i] in seen:
            seen[a[i]] = (seen[a[i]][0], i)
        else:
            seen[a[i]] = (i, i)
    buckets = {}
    for i in range(len(a)):
        key = 2 * i + 1
        if key in buckets:
            buckets[key].append(a[i])
        else:
            buckets[key] = [a[i]]
    for element in seen:
        first, second = seen[element]
        key = first + second + 1
        if radius[key] < second - first:
            continue
        if key in buckets:
            buckets[key].append(element)
        else:
            buckets[key] = [element]
    return buckets

# Clause best_mex [Confidence: 1.00]
def best_mex(buckets):
    best = 0
    for key in buckets:
        present = set(buckets[key])
        step = 0
        while step in present:
            step += 1
        if step > best:
            best = step
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        radius = palindrome_radii(a)
        out.append(best_mex(centre_values(a, radius)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

