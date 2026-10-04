import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + 2 * n])
        pos += 2 * n
    return cases


# --- clause: palindrome_radii :: (a: list[int]) -> list[int] ---
def palindrome_radii(a):
    spaced = [-1]
    for item in a:
        spaced.append(item)
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


# --- clause: centre_values :: (a: list[int], radius: list[int]) -> dict[int, list[int]] ---
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
    for item in seen:
        first, second = seen[item]
        key = first + second + 1
        if radius[key] < second - first:
            continue
        if key in buckets:
            buckets[key].append(item)
        else:
            buckets[key] = [item]
    return buckets


# --- clause: best_mex :: (buckets: dict[int, list[int]]) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        radius = palindrome_radii(a)
        out.append(best_mex(centre_values(a, radius)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
