v = input()
n = int(input())
r = [0] * n

for i, x in enumerate(map(int, v.split(", "))):
    r[i % n] += x

print(r)
