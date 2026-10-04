import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = [0] + list(map(int, input().split()))
        pos = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            pos[a[i]].append(i)

        b = [0] * (n + 1)
        used_person = [False] * (n + 1)
        used_value = [False] * (n + 1)
        score = 0

        for v in range(1, n + 1):
            chosen = 0
            for i in pos[v]:
                if i != v:
                    chosen = i
                    break
            if chosen:
                b[chosen] = v
                used_person[chosen] = True
                used_value[v] = True
                score += 1

        free_people = []
        free_values = []
        for i in range(1, n + 1):
            if not used_person[i]:
                free_people.append(i)
            if not used_value[i]:
                free_values.append(i)

        k = len(free_people)
        if k:
            free_values.sort(key=lambda x: x in set(free_people))
            for i, v in zip(free_people, free_values):
                b[i] = v

            bad = [idx for idx in range(k) if free_people[idx] == b[free_people[idx]]]
            if len(bad) == 1:
                x = free_people[bad[0]]
                for y in range(1, n + 1):
                    if used_person[y] and b[y] != x and a[y] != b[x]:
                        b[x], b[y] = b[y], b[x]
                        break
            elif len(bad) > 1:
                vals = [b[free_people[idx]] for idx in bad]
                vals = vals[1:] + vals[:1]
                for idx, v in zip(bad, vals):
                    b[free_people[idx]] = v

        out.append(str(score))
        out.append(" ".join(map(str, b[1:])))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
