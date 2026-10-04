n = int(input())

database = set()
count = {}

for _ in range(n):
    name = input().strip()
    
    if name not in database:
        database.add(name)
        print("OK")
    else:
        i = count.get(name, 0) + 1
        while name + str(i) in database:
            i += 1
        new_name = name + str(i)
        database.add(new_name)
        count[name] = i
        print(new_name)
