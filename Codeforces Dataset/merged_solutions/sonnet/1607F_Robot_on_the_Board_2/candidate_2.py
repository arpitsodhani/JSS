# CLAUSE: setup_environment
import sys

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    t = int(data[p])
    p += 1
    ans = []
    step = {
        76: (0, -1),
        82: (0, 1),
        85: (-1, 0),
        68: (1, 0),
    }

# CLAUSE: solve_logic
    for _ in range(t):
        n = int(data[p])
        m = int(data[p + 1])
        p += 2
        board = data[p:p + n]
        p += n
        total = n * m
        nxt = [-1] * total
        for r, row in enumerate(board):
            base = r * m
            for c, ch in enumerate(row):
                dr, dc = step[ch]
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    nxt[base + c] = nr * m + nc

        color = [0] * total
        dist = [0] * total
        where = [-1] * total

        for s in range(total):
            if color[s]:
                continue
            trail = []
            v = s
            while v != -1 and color[v] == 0:
                color[v] = 1
                where[v] = len(trail)
                trail.append(v)
                v = nxt[v]

            if v == -1:
                length = 0
                for u in trail[::-1]:
                    length += 1
                    dist[u] = length
            elif color[v] == 2:
                length = dist[v]
                for u in trail[::-1]:
                    length += 1
                    dist[u] = length
            else:
                start = where[v]
                length = len(trail) - start
                for k in range(start, len(trail)):
                    dist[trail[k]] = length
                for k in range(start - 1, -1, -1):
                    length += 1
                    dist[trail[k]] = length

            for u in trail:
                color[u] = 2
                where[u] = -1

        best_cell = 0
        best_dist = dist[0]
        for i in range(1, total):
            if dist[i] > best_dist:
                best_dist = dist[i]
                best_cell = i
        ans.append(str(best_cell // m + 1) + " " + str(best_cell % m + 1) + " " + str(best_dist))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
