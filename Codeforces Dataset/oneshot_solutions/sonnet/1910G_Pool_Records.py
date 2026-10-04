import sys

def generate_meetings(d1, d2, count):
    meetings = []
    i, j = 1, 0
    
    while len(meetings) < count:
        next_same = i * d1
        next_opp = (2 * j + 1) * d2
        
        if next_same < next_opp:
            meetings.append(next_same)
            i += 1
        elif next_same > next_opp:
            meetings.append(next_opp)
            j += 1
        else:
            meetings.append(next_same)
            i += 1
            j += 1
    
    return meetings

def get_divisors(n):
    divs = []
    i = 1
    while i * i <= n and i <= 100000:
        if n % i == 0:
            divs.append(i)
            if i != n // i and n // i <= 10**9:
                divs.append(n // i)
        i += 1
    return divs

def is_valid(times):
    n = len(times)
    if n == 0:
        return True
    
    all_divs = set()
    for t in times:
        all_divs.update(get_divisors(t))
    
    for d1 in all_divs:
        for d2 in all_divs:
            if d1 != d2:
                if generate_meetings(d1, d2, n) == times:
                    return True
    
    return False

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    for _ in range(T):
        n = int(input_data[idx])
        idx += 1
        times = []
        for i in range(n):
            times.append(int(input_data[idx]))
            idx += 1
        
        if is_valid(times):
            print("VALID")
        else:
            print("INVALID")

main()
