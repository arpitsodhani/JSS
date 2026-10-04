def get_rotations(a, b, c, d):
    return [
        ((a, b), (c, d)),  # 0°
        ((c, a), (d, b)),  # 90°
        ((d, c), (b, a)),  # 180°
        ((b, d), (a, c))   # 270°
    ]

def canonical_form(a, b, c, d):
    return min(get_rotations(a, b, c, d))

n = int(input())
canonical_forms = set()

for _ in range(n):
    line = input().strip()
    a, b, c, d = [int(x) for x in line]
    canonical_forms.add(canonical_form(a, b, c, d))

print(len(canonical_forms))
