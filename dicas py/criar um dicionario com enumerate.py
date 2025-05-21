arr = [37, 5, 1, 4, 2, 3, 3, 1, 5]

d = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}

print(d)

for i in enumerate(sorted(set(arr))):
    print(i)

