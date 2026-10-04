# Clause setup_environment [Confidence: 0.40]
import sys

def prime_table(limit):
    prime = [True] * (limit + 1)
    if limit >= 0:
        prime[0] = False
    if limit >= 1:
        prime[1] = False
    d = 2
    while d * d <= limit:
        if prime[d]:
            step_start = d * d
            prime[step_start:limit + 1:d] = [False] * (((limit - step_start) // d) + 1)
        d += 1
    return prime


# Clause solve_logic [Confidence: 0.80]
def count_for_array(n, e, arr, prime):
    answer = 0
    for offset in range(e):
        chain = arr[offset:n:e]
        stops = [-1]
        for i, value in enumerate(chain):
            if value != 1:
                stops.append(i)
        stops.append(len(chain))

        for j in range(1, len(stops) - 1):
            middle = stops[j]
            if prime[chain[middle]]:
                answer += (middle - stops[j - 1]) * (stops[j + 1] - middle) - 1
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    tests = []
    maximum = 0
    for _ in range(data[0]):
        n, e = data[at], data[at + 1]
        at += 2
        arr = data[at:at + n]
        at += n
        tests.append((n, e, arr))
        maximum = max(maximum, max(arr))

    prime = make_sieve(maximum)
    answers = [str(count_for_array(n, e, arr, prime)) for n, e, arr in tests]
    sys.stdout.write("\n".join(answers))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


