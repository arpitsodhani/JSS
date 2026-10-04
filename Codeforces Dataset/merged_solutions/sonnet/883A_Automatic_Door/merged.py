import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    a = data[2]
    d = data[3]
    return n, a, d, sorted(data[4:4 + m])

# Clause count_openings [Confidence: 0.80]
def count_openings(n, a, d, clients):
    step = d // a + 1
    opens = 0
    shut = -1
    done = 0
    for moment in clients:
        limit = moment // a
        if limit > n:
            limit = n
        if done < limit:
            if a * (done + 1) <= shut:
                absorbed = shut // a
                if absorbed > limit:
                    absorbed = limit
                done = absorbed
            if done < limit:
                first = done + 1
                count = (limit - first) // step + 1
                opens += count
                last = first + step * (count - 1)
                shut = a * last + d
                done = limit
        if moment > shut:
            opens += 1
            shut = moment + d
    if done < n:
        if a * (done + 1) <= shut:
            absorbed = shut // a
            if absorbed > n:
                absorbed = n
            done = absorbed
        if done < n:
            first = done + 1
            opens += (n - first) // step + 1
    return opens

# Clause main [Confidence: 1.00]
def main():
    n, a, d, clients = read_input()
    sys.stdout.write("%d\n" % count_openings(n, a, d, clients))


if __name__ == "__main__":
    main()

