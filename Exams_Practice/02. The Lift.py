people_waiting = int(input())
wagons = [int(x) for x in input().split()]
for i in range(len(wagons)):
    while wagons[i] < 4 and people_waiting > 0:
        wagons[i] += 1
        people_waiting -= 1

if people_waiting == 0 and wagons[-1] == 4:
    print(*wagons)
else:
    if wagons[-1] != 4:
        print('The lift has empty spots!')
        print(*wagons)
    else:
        print(f"There isn't enough space! {people_waiting} people in a queue!")
        print(*wagons)
