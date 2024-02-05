contact = input()
contact_list = {}
while not contact.isdigit():
    contact_info = contact.split('-')
    contact_list[contact_info[0]] = contact_info[1]
    contact = input()
for _ in range(int(contact)):
    name = input()
    if name in contact_list:
        print(f'{name} -> {contact_list[name]}')
    else:
        print(f"Contact {name} doesn't exist")