import sys

data = sys.stdin.read().split()
n = int(data[0])
t = list(map(int, data[1:n+1]))

# Set of times when rooms were last visited
available = {0}  # Starting room was visited at minute 0
num_rooms = 1

for i in range(1, n + 1):
    ti = t[i - 1]
    if ti in available:
        # Reuse the room
        available.remove(ti)
        available.add(i)
    else:
        # Create a new room
        available.add(i)
        num_rooms += 1

print(num_rooms)
