factor = int(input())
length = int(input())
l1 = []
breaker = False
while not breaker:
    for i in range(99999):
        if len(l1) == length:
            breaker = True
        if breaker:
            break
        if i % factor == 0 and i != 0:
            l1.append(i)
print(l1)