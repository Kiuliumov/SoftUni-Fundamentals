contact = input()
contacts = {}
while not contact.isdigit():
    contact_info = contact.split('-')
    contacts[contact_info[0]] = contact_info[1]
    contact = input()
for _ in range(int(contact)):
    name = input()
    if name in contacts:
        print(f'{name} -> {contacts[name]}')
    else:
        print(f"Contact {name} doesn't exist")