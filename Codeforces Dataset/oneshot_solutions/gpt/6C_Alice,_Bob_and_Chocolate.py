import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]

i, j = 0, n - 1
alice_time = 0
bob_time = 0
alice = 0
bob = 0

while i <= j:
    if alice_time <= bob_time:
        alice_time += a[i]
        alice += 1
        i += 1
    else:
        bob_time += a[j]
        bob += 1
        j -= 1

print(alice, bob)
