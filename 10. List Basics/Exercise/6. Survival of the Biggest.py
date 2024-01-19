given_array = list(map(int,input().split(' ')))
num = int(input())
for i in range(num):
    given_array.remove(min(given_array))

print(', '.join(map(str,given_array)))
