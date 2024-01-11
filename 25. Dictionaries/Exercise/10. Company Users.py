command = input()
data = {}
while command != 'End':
    command_parts = command.split(' -> ')
    company,ID = command_parts
    if company not in data:
        data[company] = []
    data[company].append(ID)
for company,ids in data.items():
    print(company)
    ids = list(set(ids))
    for id in ids:
        print(f'-- {id}')