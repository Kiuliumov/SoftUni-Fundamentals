n = int(input())
chair_count = 0
visitors_count = 0
is_enough = True
for number_of_room in range(1,n + 1):
    chairs,visitors = input().split(' ')
    chairs = len(chairs)
    visitors = int(visitors)
    if visitors > chairs:
        print(f'{visitors - chairs} more chairs needed in room {number_of_room}')
        is_enough = False
    else:
        chair_count += chairs
        visitors_count += visitors
if is_enough:
    print(f'Game On, {chair_count - visitors_count} free chairs left')