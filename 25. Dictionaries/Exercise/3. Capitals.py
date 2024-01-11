countries = input().split(', ')
capitals = input().split(', ')
packs = zip(countries,capitals)
dict_of_countries = {}
for pack in packs:
    dict_of_countries[pack[0]] = pack[1]
for country,capital in dict_of_countries.items():
    print(f'{country} -> {capital}')
