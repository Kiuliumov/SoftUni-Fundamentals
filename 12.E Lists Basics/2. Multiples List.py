length = int(input())
factor = int(input())
l1 = [range(1,length+1)]
for i in range(len(l1)):
    l1[i] *= factor
print(l1)
